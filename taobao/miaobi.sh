#!/bin/bash

case $1 in
zhifubao)
    startx=318
    starty=1437
    adb shell input tap ${startx} ${starty}
    sleep 3
    adb shell input keyevent 4
    sleep 3

    i=0
    while [[ $i -lt 5 ]];
    do
        let i=$i+1

        # adb shell input tap 201 1782
        adb shell input tap ${startx} ${starty}
        sleep 3

        adb shell input draganddrop 886 1977 900 1960 200
        sleep 3
        adb shell input draganddrop 866 652 950 658 200
        sleep 22

        echo "adb input return"
        adb shell input keyevent 4
        sleep 3

        adb shell input keyevent 4
        sleep 3

    done

    ;;
*)
    while true
    do
        adb shell input draganddrop  870 1470 900 150 200
        sleep 3
        adb shell input draganddrop  897 2032 901 2040 200
        sleep 3
        adb shell input draganddrop  829 1296 922 1303 200
        sleep 22

        echo "adb input return"
        adb shell input keyevent 4
        sleep 3

        adb shell input keyevent 4
        sleep 3
    done
    ;;
esac

