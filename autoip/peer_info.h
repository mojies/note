#ifndef __M_PEER_H
#define __M_PEER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <stdint.h>

#include <netinet/ip.h>

// seconds
#define PEER_DEAD_TIME          10

#define PEER_MAX_CAPACITY       10

typedef struct {
    uint8_t     mac[6];
    struct in_addr
                ip;
    int8_t      is_set;
    uint64_t    sec;
}m_dev_table;

extern int peer_init( void );
extern int peer_update( void );
extern m_dev_table *peer_find_via_mac( uint8_t mac[6] );
extern m_dev_table *peer_find_via_ip( struct in_addr ip );
extern int peer_add_dev( uint8_t mac[6], struct in_addr ip );

#endif
