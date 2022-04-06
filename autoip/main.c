#include <stdio.h>
#include <assert.h>

#include <unistd.h>

#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h> /* the L2 protocols */
#include <sys/types.h>
#include <ifaddrs.h>

#include "config_if.h"
#include "arp.h"

int main( int argc, char *argv[] ) {
    int             ret = 0;
    int             count = 0;

    struct in_addr  addr;
    struct in_addr  netmask;
    struct in_addr  broadcast;

    inet_aton( "255.255.0.0", &netmask );
    inet_aton( "169.254.255.255", &broadcast );

    while( 1 ){
        ret = if_config_gen_new_ipv4( "eth0", &addr );
        printf( "ret -> %d\n", ret );
        if( ret == -1 ){
            // TODO err log
            break;
        }

        net_print_ipv4( "set", addr );
        net_print_ipv4( "set", netmask );
        net_print_ipv4( "set", broadcast );

        ret = net_set_if_ip( "eth0", addr, netmask, broadcast );
        printf( "ret -> %d\n", ret );
        if( ret == -1 ){
            // TODO err log
            break;
        }

        ret = arp_restart( "eth0", addr );
        printf( "ret -> %d\n", ret );
        assert( ret ==  0 );

        while(1){
            int ret;
            ret = arp_is_conflict();
            assert( ret != -1 );

            if( ret == 1 ){
                printf( "conflict ---->\n" );
                break;
            }else{
                printf( "detect agin ---->\n" );
                sleep(1);
            }
        }
    }

    return 0;
}

