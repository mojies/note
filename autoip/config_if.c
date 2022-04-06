#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <unistd.h>

#include "md5.h"
#include "net_tools.h"

#include "config_if.h"

static char         *l_if_name = NULL;
static uint8_t      l_if_mac[ 6 ];
static uint8_t      l_seed[64];

int if_config_gen_new_ipv4( const char *if_name, struct in_addr *addr ){
    bool            need_get_mac = false;
    int             if_name_len = strlen( if_name );
    mbedtls_md5_context
                    md5_ctx;
    uint8_t         hash_code[16];
    unsigned long   ipv4 = 0;
    int             i;

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

    ipv4 |= 169<<24;
    ipv4 |= 254<<16;
    while( 1 ){
        mbedtls_md5_init( &md5_ctx );
        mbedtls_md5_starts( &md5_ctx );
        mbedtls_md5_update( &md5_ctx, l_seed, 64 );
        mbedtls_md5_finish( &md5_ctx, hash_code );
        mbedtls_md5_free( &md5_ctx );

        memcpy( &l_seed[6], hash_code, 16 );

        for( i = 0; i < 16; i++ ){
            if( hash_code[i] == 0 || hash_code[i] == 255 )
                continue;
            ipv4 |= (hash_code[i])<<8;
        }
        if( i == 16 ) continue;

        i++; i %= 16;
        ipv4 |= hash_code[i];

        break;
    }

    addr->s_addr = ipv4;
    return 0;
}

// unsigned long = inet_addr( "xx.xx.xx.xx" );
int net_set_if_ip( const char *if_name,
        struct in_addr ip, struct in_addr netmask, struct in_addr broadcast ){

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

    strncpy(ifr.ifr_name, if_name, IFNAMSIZ);
    memset(&sin, 0, sizeof(struct sockaddr));
    sin.sin_family = AF_INET;

    sin.sin_addr.s_addr = ip.s_addr;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl( fd, SIOCSIFADDR, &ifr ) < 0)
        return -1;

    sin.sin_addr.s_addr = netmask.s_addr;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl( fd, SIOCSIFNETMASK, &ifr ) < 0)
        return -1;

    sin.sin_addr.s_addr = broadcast.s_addr;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl( fd, SIOCSIFBRDADDR, &ifr ) < 0)
        return -1;

    if( ioctl(fd, SIOCGIFFLAGS, &ifr)  < 0 )
        return -1;
    ifr.ifr_flags |= IFF_UP | IFF_RUNNING;
    if( ioctl(fd, SIOCSIFFLAGS, &ifr) < 0 )
        return -1;

    close( fd );
    return 0;
}

