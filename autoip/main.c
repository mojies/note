#include <stdio.h>
#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h> /* the L2 protocols */
#include <sys/types.h>
#include <ifaddrs.h>

#include "config_if.h"

int main( int argc, char *argv[] ) {
    uint8_t         addr[ 4 ];
    int             ret = 0;
    int             count = 0;

    while( 1 ){
        ret = if_config_gen_new_ipv4( "eth0", addr );
        printf( "ret -> %d\n", ret );

        printf( "ip addr -> " );
        for( int j = 0; j < 4; j++ ){
            printf( "%d.", (int)addr[j] );
        }
        printf( "\n" );

        count++;
        if( count > 2 )
            break;
    }

    return 0;
}

