#ifndef __M_NET_TOOLS_H
#define __M_NET_TOOLS_H

int net_get_if_mac_addr( const char *if_name, uint8_t mac_addr[6] );
extern void net_show_if_info(void);

#endif
