#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "md5.h"
#include "net_tools.h"

#include <sys/ioctl.h>
#include <net/if.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>

static char         *l_if_name = NULL;
static uint8_t      l_if_mac[ 6 ];
static uint8_t      l_seed[64];

int if_config_gen_new_ipv4( const char *if_name, uint8_t addr[4] ){
    bool            need_get_mac = false;
    int             if_name_len = strlen( if_name );
    mbedtls_md5_context
                    md5_ctx;
    uint8_t         hash_code[16];
    uint8_t         ipv4[4];

    if( if_name == NULL || if_name_len <= 0 || if_name_len >= 12 )
        return -1;

    if( l_if_name == NULL ){
        l_if_name = strdup( if_name );
        need_get_mac = true;
    }else{
        if( strcmp( l_if_name, if_name ) != 0 ){
            free( l_if_name );
            l_if_name = strdup( if_name );
            need_get_mac = true;
        }
    }

    if( need_get_mac ){
        if( net_get_if_mac_addr( if_name, l_if_mac ) ){
            // TODO error log
            return -1;
        }
        memcpy( l_seed, l_if_mac, 6 );
    }

    ipv4[0] = 169;
    ipv4[1] = 254;
    while( 1 ){
        mbedtls_md5_init( &md5_ctx );
        mbedtls_md5_starts( &md5_ctx );
        mbedtls_md5_update( &md5_ctx, l_seed, 64 );
        mbedtls_md5_finish( &md5_ctx, hash_code );
        mbedtls_md5_free( &md5_ctx );

        memcpy( &l_seed[6], hash_code, 16 );
        ipv4[2] = hash_code[0];
        ipv4[3] = hash_code[1];

        if( ipv4[2] == 0 || ipv4[2] == 255 )
            continue;

        break;
    }

    memcpy( addr, ipv4, 4 );

    return 0;
}

// unsigned long = inet_addr( "xx.xx.xx.xx" );
int net_set_if_ip( const char *name,
        unsigned long ip, unsigned long netmask. unsigned long broadcast ){

    struct ifreq        ifr;
    struct sockaddr_in  sin;
    int                 fd;
    int                 selector;
    unsigned char       mask;

    char                *p;

    fd = socket( AF_INET, SOCK_DGRAM, 0 );
    if( fd < 0 ){
        return -1;
    }

    strncpy(ifr.ifr_name, name, IFNAMSIZ);
    memset(&sin, 0, sizeof(struct sockaddr));
    sin.sin_family = AF_INET;

    sin.sin_addr.s_addr = ip;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl( fd, SIOCSIFADDR, &ifr ) < 0)
        return -1;

    sin.sin_addr.s_addr = netmask;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl( fd, SIOCSIFNETMASK, &ifr ) < 0)
        return -1;

    sin.sin_addr.s_addr = broadcast;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl( fd, SIOCSIFBRDADDR, &ifr ) < 0)
        return -1;

    if( ioctl(sockfd, SIOCGIFFLAGS, &ifr)  < 0 )
        return -1;
    ifr.ifr_flags |= IFF_UP | IFF_RUNNING;
    if( ioctl(sockfd, SIOCSIFFLAGS, &ifr) < 0 )
        return -1;

    close( fd );
    return 0;
}

