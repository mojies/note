#include <stdio.h>
#include <string.h>

#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h> /* the L2 protocols */
#include <sys/types.h>
#include <ifaddrs.h>


void net_show_if_info( void ){
    struct ifaddrs         *if_addr;
    struct ifaddrs         *ifa;
    int                     rc;
    int                     i  =0;

    rc = getifaddrs( &if_addr );
    if (rc) {
        printf( "getifaddrs fail");
        return;
    }

    for( ifa = if_addr; ifa; ifa = ifa->ifa_next ){
        printf( "IF: %d\n", i );
        i++;

        printf( "    IF Name: %s\n", ifa->ifa_name );
        printf( "    IF FLAGS: %08x\n", ifa->ifa_flags );
        printf( "    IF AF Family: %08x\n", ifa->ifa_addr->sa_family );
        printf( "    IF AF Family: %s\n",
                (ifa->ifa_addr->sa_family == AF_PACKET)?"IS AF_PACKET":"NO" );
        if( ifa->ifa_addr->sa_family == AF_PACKET ){
            printf( "    IF MAC Addr: " );
            for( int j = 0; j < 6; j++ )
                printf( "%02x.", (unsigned int)(
                            ((struct sockaddr_ll*)ifa->ifa_addr)->sll_addr[j]) );
            printf( "\n" );
        }
    }

    freeifaddrs( if_addr );
}

int net_get_if_mac_addr( const char *if_name, uint8_t mac_addr[6] ){
    struct ifaddrs         *if_addr;
    struct ifaddrs         *ifa;
    int                     rc;
    int                     i  =0;
    int                     ret = -1;

    rc = getifaddrs( &if_addr );
    if (rc) {
        printf( "getifaddrs fail");
        return -1;
    }

    for( ifa = if_addr; ifa; ifa = ifa->ifa_next ){
        if( ifa->ifa_addr == NULL )
            continue;
        if( ifa->ifa_addr->sa_family != AF_PACKET )
            continue;
        if( ifa->ifa_name && strcmp( ifa->ifa_name, if_name ) == 0 ){
            memcpy( mac_addr, ((struct sockaddr_ll*)ifa->ifa_addr)->sll_addr, 6 );
            ret = 0;
            break;
        }
    }
    freeifaddrs( if_addr );
    return ret;
}

#if 0
int check_device( const char *if_name, struct run_state *ctl)
{
    int                     rc;
    struct ifaddrs         *if_addr;
    struct ifaddrs         *ifa;
    int                     n = 0;

    rc = getifaddrs( &if_addr );
    if (rc) {
        error(0, errno, "getifaddrs");
        return -1;
    }

    for( ifa = if_addr; ifa; ifa = ifa->ifa_next ){
        if( !ifa->ifa_addr )
            continue;
        /*
         * By default, all packets of the specified protocol type are passed
         * to a packet socket.  To get packets only from a specific
         * interface use bind(2) specifying an address in a struct
         * sockaddr_ll to bind the packet socket to an interface.  Fields
         * used for binding are sll_family (should be AF_PACKET),
         * sll_protocol, and sll_ifindex.
         * */
        if( ifa->ifa_addr->sa_family != AF_PACKET )
            continue;

        // check if_name is correct
        if( if_name && ifa->ifa_name && strcmp( ifa->ifa_name, if_name ) )
            continue;

        if( check_ifflags(ctl, ifa->ifa_flags) < 0 )
            continue;

        if( !((struct sockaddr_ll *)ifa->ifa_addr)->sll_halen )
            continue;

        if( !ifa->ifa_broadaddr )
            continue;

        ctl->device.ifa = ifa;

        if (n++)
            break;
    }

    if (n == 1 && ctl->device.ifa) {
        ctl->device.ifindex = if_nametoindex(ctl->device.ifa->ifa_name);
        if (!ctl->device.ifindex) {
            error(0, errno, "if_nametoindex");
            freeifaddrs( if_addr );
            return -1;
        }
        ctl->device.name = ctl->device.ifa->ifa_name;
        return 0;
    }
    return 1;
}

#endif
