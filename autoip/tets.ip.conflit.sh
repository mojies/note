#!/bin/bash

IF=eth0
ETH0_MAC=$(cat /sys/class/net/${IF}/address)
SEED=${ETH0_MAC}


set_ip_addr(){
    ifconfig ${IF} $1
}

while true
do

    SEED=${SEED}${ETH0_MAC}
    echo "SEED -> ${SEED}"
    
    HASH=$(echo "${SEED}" | md5sum - | cut -d' ' -f1)
    
    SEED=${HASH}
    echo "HASH -> ${HASH}"
    
    IP3=169
    IP2=254
    
    IP1=$((16#${HASH:0:2}))
    IP0=$((16#${HASH:2:2}))
    
    if [ "${IP1}" = "0" ]; then
        continue
    fi
    
    if [ "${IP1}" = "255" ]; then
        continue
    fi
    
    IP=${IP3}.${IP2}.${IP1}.${IP0}
    
    echo "IP -> ${IP}"
    
    set_ip_addr ${IP}
    sleep 0.2

    while true
    do
        echo "test IP conflict... "
        arping -c 2 ${IP}
        if [ $? -eq 0 ]; then
            echo "test IP conflicted, start change ip"
            break;
        fi
        sleep 5
    done
done
