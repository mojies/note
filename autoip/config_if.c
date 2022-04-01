#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "md5.h"
#include "net_tools.h"

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

static int lf_set_ip_using( const char *name, int c, unsigned long ip );

int net_set_if_ipv4( const char *name, unsigned long ip ){
    return lf_set_ip_using( name, SIOCSIFADDR, ip);
}

int net_set_if_netmask( const char *name, unsigned long ip ){
    return lf_set_ip_using( name, SIOCSIFBRDADDR, ip);
}

int net_set_if_broadcast( const char *name, unsigned long ip ){
    return lf_set_ip_using( name, SIOCSIFBRDADDR, ip);
}

static int lf_set_ip_using( const char *name, int c, unsigned long ip ){
    struct ifreq ifr;
    struct sockaddr_in sin;

    safe_strncpy(ifr.ifr_name, name, IFNAMSIZ);
    memset(&sin, 0, sizeof(struct sockaddr));
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = ip;
    memcpy(&ifr.ifr_addr, &sin, sizeof(struct sockaddr));
    if (ioctl(skfd, c, &ifr) < 0)
        return -1;
    return 0;
}


