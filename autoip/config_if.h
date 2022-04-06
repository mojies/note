#ifndef __M_CONFIG_IF_H
#define __M_CONFIG_IF_H

#include <stdint.h>
#include <stdbool.h>

#include <arpa/inet.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>

extern int if_config_gen_new_ipv4( const char *if_name, struct in_addr *addr );
extern int net_set_if_ip( const char *if_name,
        struct in_addr ip, struct in_addr netmask, struct in_addr broadcast );

#endif
