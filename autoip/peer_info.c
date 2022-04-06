#include <sys/time.h>

#include "peer_info.h"
#include "mdebug.h"

static m_dev_table      l_tb[ PEER_MAX_CAPACITY ];

int peer_init( void ){
    memcpy( l_tb, 0, sizeof(l_tb) );
}

int peer_update( void ){
    struct timeval          tv;
    int                     i;

    gettimeofday( &tv, NULL );
    for( i = 0; i < PEER_MAX_CAPACITY; i++ )
        if( l_tb[ i ].is_set == 1 )
            if( (tv.tv_sec - l_tb[i].sec) >= PEER_DEAD_TIME )
                l_tb[ i ].is_set = 0;

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

    printf( "mojies -------------------> %d\n", __LINE__ );
    mdebug_print_hex( (void*)&ip, sizeof(struct in_addr) );
    for( i = 0; i < PEER_MAX_CAPACITY; i++ ){
        if( l_tb[ i ].is_set == 0 )
            continue;

    mdebug_print_hex( (void*)&l_tb[ i ].ip, sizeof(struct in_addr) );
        if( l_tb[ i ].ip.s_addr == ip.s_addr ){
            return &l_tb[ i ];
        }
    }

    return NULL;
}

int peer_add_dev( uint8_t mac[6], struct in_addr ip ){
    m_dev_table             *tb;
    struct timeval          tv;
    int                     ilde = -1;
    int                     oldest = -1;
    uint64_t                oldest_seconds;

    int                     i;

    gettimeofday( &tv, NULL );

    for( i = 0; i < PEER_MAX_CAPACITY; i++ )
        if( l_tb[ i ].is_set == 1 )
            if( (tv.tv_sec - l_tb[i].sec) >= PEER_DEAD_TIME )
                l_tb[ i ].is_set = 0;

    tb = peer_find_via_mac( mac );

    if( tb ){
        // TODO err log
        tb->ip = ip;
        tb->is_set = 1;
        tb->sec = tv.tv_sec;
        return 0;
    }

    for( i = 0; i < PEER_MAX_CAPACITY; i++ ){
        if( l_tb[ i ].is_set ){
            uint64_t diff = tv.tv_sec - l_tb[ i ].sec;
            if( diff > oldest_seconds ){
                oldest = i;
                oldest_seconds = l_tb[ i ].sec;
            }
        }else{
            ilde = i;
            break;
        }
        // find no set
        // find oldest
    }

    if( ilde != -1 ){
        memcpy( l_tb[ ilde ].mac, mac, 6 );
        l_tb[ ilde ].ip = ip;
        l_tb[ ilde ].is_set = 1;
        l_tb[ ilde ].sec = tv.tv_sec;

    }else if( oldest != -1 ){
        memcpy( l_tb[ oldest ].mac, mac, 6 );
        l_tb[ oldest ].ip = ip;
        l_tb[ oldest ].is_set = 1;
        l_tb[ oldest ].sec = tv.tv_sec;

    }
    return 0;
}



// active




