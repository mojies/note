#include <string,h>
#include <stdlib.h>
#include "peer_info.h"

static m_dev_table      l_tb[ PEER_MAX_CAPACITY ];
static int              l_tb_size = 0;

int peer_init( void ){
    memcpy( l_tb_size, 0, sizeof(l_tb) );
}

int peer_update( void ){
    struct timeval          tv;

    gettimeofday( &tv, NULL );
    if( (tv.tv_sec - sec) >= PEER_DEAD_TIME ){
        l_tb[ i ].is_set = 0;
    }

    return 0;
}

m_dev_table *peer_find_via_mac( uint8_t mac[6] ){
    int                     i;

    for( i = 0; i < PEER_MAX_CAPACITY; i++ ){
        if( l_tb[ i ].is_set == 0 )
            continue;

        if( memcmp( l_tb[ i ].mac, mac, 6 ) == 0 ){
            return &l_tb[ i ];
        }
    }

    return NULL;
}

m_dev_table *peer_find_via_ip( struct in_addr ip ){
    int                     i;

    for( i = 0; i < PEER_MAX_CAPACITY; i++ ){
        if( l_tb[ i ].is_set == 0 )
            continue;

        if( l_tb[ i ].ip.s_addr == ip.s_addr ){
            return &l_tb[ i ];
        }
    }

    return NULL;
}

int peer_add_dev( uint8_t mac[6], struct in_addr ip ){
    m_dev_table             *tb;
    struct timeval          tv;
    int                     ilde_index = -1;
    int                     oldest_index = -1;
    uint64_t                oldest_seconds;

    int                     i;

    gettimeofday( &tv, NULL );
    if( (tv.tv_sec - sec) >= PEER_DEAD_TIME )
        l_tb[ i ].is_set = 0;

    tb = peer_find_via_mac( mac );

    if( tb ){
        // TODO err log
        tb->ip = ip;
        tb->is_set = 1;
        tb->sec = tv.tv_sec;
    }

    for( i = 0; i < PEER_MAX_CAPACITY; i++ ){
        if( l_tb[ i ].is_set ){
            uint64_t diff = tv.tv_sec - l_tb[ i ].sec;
            if( diff > oldest_seconds ){
                oldest_index = i;
                oldest_seconds = l_tb[ i ].sec;
            }
        }else{
            ilde_index = i;
            break;
        }
        // find no set
        // find oldest
    }

    if( ilde_index != -1 ){
        memcpy( l_tb[ ilde_index ].mac, mac, 6 );
        l_tb[ ilde_index ].ip = ip;
        l_tb[ ilde_index ].is_set = 1;
        l_tb[ ilde_index ].sec = tv.tv_sec;

    }else{
        memcpy( l_tb[ oldest_index ].mac, mac, 6 );
        l_tb[ oldest_index ].ip = ip;
        l_tb[ oldest_index ].is_set = 1;
        l_tb[ oldest_index ].sec = tv.tv_sec;

    }

    return 0;
}



// active




