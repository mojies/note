#ifndef __M_CONFIG_IF_H
#define __M_CONFIG_IF_H

#include <stdint.h>
#include <stdbool.h>

extern int if_config_gen_new_ipv4( const char *if_name, uint8_t addr[4] );
extern int net_set_if_ipv4( const char *name, unsigned long ip );
extern int net_set_if_netmask( const char *name, unsigned long ip );
extern int net_set_if_broadcast( const char *name, unsigned long ip );

#endif
