#include <assert.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <pthread.h>

#include <arpa/inet.h>
#include <errno.h>
#include <ifaddrs.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/rtnetlink.h>
#include <netdb.h>
#include <net/if_arp.h>
#include <net/if.h>
#include <poll.h>
#include <sys/param.h>
#include <sys/signalfd.h>
#include <sys/timerfd.h>
#include <unistd.h>
#include <pthread.h>

#include "iputils_common.h"
#include "peer_info.h"

#ifndef AX25_P_IP
# define AX25_P_IP        0xcc    /* ARPA Internet Protocol     */
#endif

#define FINAL_PACKS        2

#define DL_TIMER_LIMIT_MS       300

// =============================================================================
static void lf_init_param( void );

static int lf_get_if_info( const char *if_name, int *if_index,
        struct sockaddr *addr, struct sockaddr *netmask,
        struct sockaddr *broadcast );

static int lf_set_if_dont_route( const char *if_name, struct in_addr *dest,
        struct in_addr *src );

static int lf_get_me_and_he( struct sockaddr *broadcast, int fd,
        struct sockaddr_storage *me, struct sockaddr_storage *he );

static int lf_get_ping_socket( int if_index );

static void *lf_detect_conflict_thrd( void *pdata );

static int lf_send_arp_request_package( int fd,
        struct sockaddr_storage *me, struct sockaddr_storage *he,
        struct in_addr   *src, struct in_addr   *dst );

static int lf_get_mac_and_ip( const uint8_t *buf, size_t len,
        uint8_t mac[8], struct in_addr *ip );

// =============================================================================
static int              l_if_index = -1;
static char             l_if_name[12];
static struct sockaddr  l_if_address;
static struct sockaddr  l_if_netmask;
static struct sockaddr  l_if_broadcast;

static struct in_addr   l_src_addr;
static struct in_addr   l_dst_addr;

struct sockaddr_storage l_me;
struct sockaddr_storage l_he;

static int              l_fd = -1;

#define ARP_STAT_THRD_START  0x0001
#define ARP_STAT_THRD_EXIT   0x0002
volatile static uint32_t
                        l_stat = 0;
volatile static pthread_t
                        l_thrd_id;

// =============================================================================
int arp_start( const char *if_name, struct in_addr self_ip ){
    int ret;

    lf_init_param();

    // param check
    assert( if_name != NULL && *if_name != '\0' );
    assert( strlen( if_name ) < 12 );

    strcpy( l_if_name, if_name );

    // legality check
#if 1
    // if( strncmp( self_ip, "169.254.", sizeof( "169.254." ) ) ){
    if( (self_ip.s_addr & 0xFFFF0000) != 0xA9FE0000 ){
        // TODO error log
        return -1;
    }
#endif

    if( lf_get_if_info( if_name, &l_if_index,
                &l_if_address, &l_if_netmask, &l_if_broadcast ) ){
        // TODO error log
        return -1;
    }

    l_src_addr = l_dst_addr = self_ip;

    if( lf_set_if_dont_route( if_name, &l_dst_addr, &l_src_addr ) ){
        // TODO error log
        return -1;
    }

    // get socket fd
    if( (l_fd = lf_get_ping_socket( l_if_index ) ) < 0 ){
        // TODO error log
        return -1;
    }

    // me he
    if( lf_get_me_and_he( &l_if_broadcast, l_fd, &l_me, &l_he ) ){
        // TODO error log
        goto err;
    }

    if( pthread_create( (pthread_t*)&l_thrd_id, NULL, lf_detect_conflict_thrd, NULL ) ){
        // TODO error log
        goto err;
    }

    l_stat |= ARP_STAT_THRD_START;
    return 0;
err:
    close( l_fd );
    return -1;
}

int arp_stop( void ){
    if( l_stat & ARP_STAT_THRD_START ){
        l_stat |= ARP_STAT_THRD_EXIT;
        // TODO unlock --> risk
        pthread_join( l_thrd_id, NULL );
    }
    return 0;
}

int arp_restart( const char *if_name, struct in_addr self_ip ){
    arp_stop();
    return arp_start( if_name, self_ip );
}

int arp_is_conflict( void ){
    m_dev_table         *dev;
    if( l_stat & ARP_STAT_THRD_START ){
        dev = peer_find_via_ip( l_dst_addr );
        if( dev ){
            return 1;
        }else{
            return 0;
        }
    }
    return -1;
}

// =============================================================================

static void lf_init_param( void ){
    // init param
    memset( &l_dst_addr, 0x00, sizeof(l_dst_addr) );
    memset( &l_src_addr, 0x00, sizeof(l_src_addr) );
    memset( &l_me, 0x00, sizeof(l_me) );
    memset( &l_he, 0x00, sizeof(l_he) );

    memset( &l_if_name, 0x00, 12 );

    memset( &l_if_address, 0x00, sizeof(l_if_address) );
    memset( &l_if_netmask, 0x00, sizeof(l_if_netmask) );
    memset( &l_if_broadcast, 0x00, sizeof(l_if_broadcast) );
    l_if_index = -1;

    l_fd = -1;
    l_stat = 0;
    l_thrd_id = -1;
}

static int lf_get_if_info( const char *if_name, int *if_index,
        struct sockaddr *addr, struct sockaddr *netmask,
        struct sockaddr *broadcast ){

    int rc;
    struct ifaddrs *all_if;
    struct ifaddrs *a_if;

    assert( if_name == NULL || *if_name == '\0' );

    if( getifaddrs(&all_if) ){
        // TODO error log
        return -1;
    }

    for (a_if = all_if; a_if; a_if = a_if->ifa_next) {
        if( a_if->ifa_addr == NULL )
            continue;
        if( a_if->ifa_addr->sa_family != AF_PACKET )
            continue;
        if ( a_if->ifa_name == NULL )
            continue;
        if( strcmp( a_if->ifa_name, if_name ) )
            continue;

        // is UP
        if( (a_if->ifa_flags & IFF_UP) == 0 )
            continue;
        // is forbiden arp or is lo
        if( a_if->ifa_flags & (IFF_NOARP | IFF_LOOPBACK) )
            continue;

        if (!((struct sockaddr_ll *)a_if->ifa_addr)->sll_halen)
            continue;

        if (a_if->ifa_addr)
            *addr = *(a_if->ifa_addr);

        if (a_if->ifa_netmask)
            *netmask = *(a_if->ifa_netmask);

        if (a_if->ifa_broadaddr)
            *broadcast = *(a_if->ifa_broadaddr);

        *if_index = if_nametoindex( a_if->ifa_name );

        break;
    }

    freeifaddrs( all_if );
    if( a_if ){
        return 0;
    }else{
        return -1;
    }
}

static int lf_set_if_dont_route( const char *if_name, struct in_addr *dest,
        struct in_addr *src ){
    struct sockaddr_in  addr;
    socklen_t           alen = sizeof(addr);
    int                 on = 1;
    int                 fd;

    assert( if_name == NULL || *if_name != 0 );

    if( ( fd = socket(AF_INET, SOCK_DGRAM, 0) ) < 0 ){
        // TODO err log
        return -1;
    }

    if( setsockopt( fd, SOL_SOCKET, SO_BINDTODEVICE,
                if_name, strlen( if_name ) + 1 ) < 0 ){
        // TODO error log
        goto err;
    }

    memset( &addr, 0, sizeof(addr) );
    addr.sin_family = AF_INET;
    addr.sin_port = htons(1025);
    addr.sin_addr = *dest;

    if( setsockopt( fd, SOL_SOCKET, SO_DONTROUTE, (char *)&on,
                sizeof(on)) < 0 ){
        // TODO err log
        goto err;
    }

    if( connect( fd, (struct sockaddr *)&addr, sizeof(addr) ) < 0 ){
        // TODO err log
        goto err;
    }

    if( getsockname( fd, (struct sockaddr *)&addr, &alen ) < 0 ){
        // TODO err log
        goto err;
    }

    *src = addr.sin_addr;
    close( fd );
    return 0;

err:
    if( fd > 0 )
        close( fd );
    return -1;
}

static int lf_get_ping_socket( int if_index ){
    struct sockaddr_storage     addr;
    socklen_t                   alen = sizeof( struct sockaddr_storage );
    int                         fd = -1;

    if( (fd = socket(PF_PACKET, SOCK_DGRAM, 0) ) < 0 ){
        // TODO error log
        return -1;
    }

    ((struct sockaddr_ll *)&addr)->sll_family = AF_PACKET;
    ((struct sockaddr_ll *)&addr)->sll_ifindex = if_index;
    ((struct sockaddr_ll *)&addr)->sll_protocol = htons(ETH_P_ARP);
    if (bind( fd, (struct sockaddr *)&addr, sizeof(addr)) < 0 ){
        // TODO err log
        goto err;
    }

    return fd;
err:
    close( fd );
    return -1;
}

static int lf_get_me_and_he( struct sockaddr *broadcast, int fd,
        struct sockaddr_storage *me, struct sockaddr_storage *he ){

    socklen_t               alen = sizeof( struct sockaddr_storage );
    struct sockaddr_ll      *sll;
    struct sockaddr_ll      *HE = (struct sockaddr_ll*)he;
    unsigned char           copy_len;

    assert( fd > 0 );
    assert( me != NULL );
    assert( he != NULL );

    if( getsockname( fd, (struct sockaddr *)me, &alen ) < 0 ){
        // TODO err log
        return -1;
    }

    if( ((struct sockaddr_ll *)me)->sll_halen == 0 ) {
        // TODO err log
        return -1;
    }

    *he = *me;

    copy_len = HE->sll_halen;
    sll = (struct sockaddr_ll *)broadcast;
    if( sll->sll_halen == copy_len ){
        memcpy( HE->sll_addr, sll->sll_addr, copy_len );
        return 0;
    }else{
        memset( HE->sll_addr, 255, copy_len );
    }
    return 0;
}

__attribute__((const)) static inline size_t sll_len(const size_t halen)
{
    const struct sockaddr_ll unused;
    const size_t len = offsetof(struct sockaddr_ll, sll_addr) + halen;

    if (len < sizeof(unused))
        return sizeof(unused);
    return len;
}

static int lf_send_arp_request_package( int fd,
        struct sockaddr_storage *me, struct sockaddr_storage *he,
        struct in_addr   *src, struct in_addr   *dst ){

    int                 err;
    unsigned char       buf[256];
    struct arphdr       *ah = (struct arphdr *)buf;
    unsigned char       *p = (unsigned char *)(ah + 1);
    struct sockaddr_ll  *ME = (struct sockaddr_ll *)me;
    struct sockaddr_ll  *HE = (struct sockaddr_ll *)he;

    ah->ar_hrd = htons(ME->sll_hatype);
    if (ah->ar_hrd == htons(ARPHRD_FDDI))
        ah->ar_hrd = htons(ARPHRD_ETHER);

    /*
     * Exceptions everywhere. AX.25 uses the AX.25 PID value not the
     * DIX code for the protocol. Make these device structure fields.
     */
    if (ah->ar_hrd == htons(ARPHRD_AX25) ||
            ah->ar_hrd == htons(ARPHRD_NETROM))
        ah->ar_pro = htons(AX25_P_IP);
    else
        ah->ar_pro = htons(ETH_P_IP);

    ah->ar_hln = ME->sll_halen;
    ah->ar_pln = 4;
    ah->ar_op  = htons(ARPOP_REQUEST);

    memcpy(p, &ME->sll_addr, ah->ar_hln);
    p += ME->sll_halen;

    memcpy(p, src, 4);
    p += 4;

    // memcpy(p, &ME->sll_addr, ah->ar_hln);
    memcpy(p, &HE->sll_addr, ah->ar_hln);
    p += ah->ar_hln;

    memcpy(p, dst, 4);
    p += 4;

    return sendto( fd, buf, p - buf, 0, (struct sockaddr *)HE,
            sll_len(ah->ar_hln));
}

static int lf_get_mac_and_ip( const uint8_t *buf, size_t len,
        uint8_t mac[8], struct in_addr *ip ){

    struct arphdr       *ah = (struct arphdr *)buf;
    uint8_t             hardware_addr_len;
    uint8_t             protocol_addr_len;

    if( buf[ 0 ] != 0x00 || buf[ 1 ] != 0x01 )
        return -1;

    if( buf[ 2 ] != 0x80 || buf[ 3 ] != 0x00 )
        return -1;

    hardware_addr_len = buf[4];
    protocol_addr_len = buf[5];

    if( buf[ 6 ] != 0x00 )
        return -1;

    // htons(ARPOP_REQUEST) htons(ARPOP_REPLY))
    if( buf[ 7 ] != 0x00 && buf[7] != 0x01 )
        return -1;

    memcpy( mac, &buf[8], 6 );
    memcpy( ip, &buf[8+4], 4 );

    return 0;
}


static void *lf_detect_conflict_thrd( void *pdata ){
    enum {
        POLLFD_TIMER,
        POLLFD_SOCKET,
        POLLFD_COUNT
    };
    struct pollfd           pfds[ POLLFD_COUNT ];

    int                     tfd;
    struct itimerspec       timerfd_val = {
        .it_interval.tv_sec = DL_TIMER_LIMIT_MS/1000,
        .it_interval.tv_nsec = DL_TIMER_LIMIT_MS*1000,
        .it_value.tv_sec = DL_TIMER_LIMIT_MS/1000,
        .it_value.tv_nsec = DL_TIMER_LIMIT_MS*1000
    };


    uint64_t                exp;
    uint64_t                total_expires = 1;

    unsigned char           packet[4096];
    ssize_t                 rlen;

    struct sockaddr_storage from;
    socklen_t               addr_len = sizeof(from);

    pthread_detach( pthread_self() );


    if( l_fd < 0 )
        goto exit;

    memset(&from, 0, sizeof(from));

    /* interval timerfd */
    if( ( tfd = timerfd_create(CLOCK_MONOTONIC, 0) ) < 0 ){
        goto exit;
    }

    if( timerfd_settime( tfd, 0, &timerfd_val, NULL ) ){
        goto exit;
    }

    pfds[POLLFD_TIMER].fd = tfd;
    pfds[POLLFD_TIMER].events = POLLIN | POLLERR | POLLHUP;

    /* socket */
    pfds[POLLFD_SOCKET].fd = l_fd;
    pfds[POLLFD_SOCKET].events = POLLIN | POLLERR | POLLHUP;
    lf_send_arp_request_package( l_fd,
            &l_me, &l_he, &l_src_addr, &l_dst_addr);

    while( ( l_stat & ARP_STAT_THRD_EXIT ) == 0 ){
        int ret;
        size_t i;

        ret = poll(pfds, POLLFD_COUNT, -1);
        if( ret <= 0 ){
            if( errno == EAGAIN )
                continue;

            l_stat |= ARP_STAT_THRD_EXIT;
            continue;
        }

        for( i = 0; i < POLLFD_COUNT; i++ ){
            if( pfds[i].revents == 0 )
                continue;

            switch( i ){
            case POLLFD_TIMER:{
                rlen = read(tfd, &exp, sizeof(uint64_t));
                if( rlen != sizeof(uint64_t) ){
                    error( 0, errno, "could not read timerfd" );
                    continue;
                }
                lf_send_arp_request_package( l_fd,
                    &l_me, &l_he, &l_src_addr, &l_dst_addr);
            }break;

            case POLLFD_SOCKET:{
                if ((rlen = recvfrom( l_fd, packet, sizeof(packet),
                                0, (struct sockaddr *)&from, &addr_len)) < 0) {

                    // TODO err log
                    if (errno == ENETDOWN)
                        continue;
                }

                if( rlen > 0 ){
                    uint8_t         mac[6];
                    struct in_addr  ip;
                    struct sockaddr_ll  *ll_from = ( struct sockaddr_ll * )&from;

                    /* Filter out wild packets */
                    if( ll_from->sll_pkttype != PACKET_HOST
                     && ll_from->sll_pkttype != PACKET_BROADCAST
                     && ll_from->sll_pkttype != PACKET_MULTICAST )
                     break;

                    if( lf_get_mac_and_ip( packet, rlen, mac, &ip ) ){
                        // TODO err log
                        break;
                    }

                    peer_add_dev( mac, ip );
                }
            }break;

            default: abort();
            }
        }
    }
exit:
    if( tfd > 0 )
        close( tfd );
    if( l_fd > 0 )
        close( l_fd );
    lf_init_param();
    pthread_exit( NULL );
    return NULL;
}


