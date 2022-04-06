#ifndef __M_ARP_H
#define __M_ARP_H


extern int arp_start( const char *if_name, struct in_addr self_ip );
extern int arp_stop( void );
extern int arp_restart( const char *if_name, struct in_addr self_ip );
extern int arp_is_conflict( void );


#endif

