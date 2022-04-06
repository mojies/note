#!/bin/bash

case $1 in

test)
    gcc -o test main.c net_tools.c config_if.c md5.c arp.c peer_info.c -lpthread
    ;;
*)
    gcc -o arp.t arping.c iputils_common.c md5.c
    # sudo ./arp.t -I eth0 -c 2 172.16.20.61
    ;;
esac
