#!/bin/bash


while true
do
	if [ "$1" = "zhifubao" ]; then
		# adb shell input draganddrop 399 1400 500 1500 200
		adb shell input tap 201 1782
		sleep 3
		adb shell input draganddrop 886 1977 900 1960 200
		sleep 3

	else
		adb shell input draganddrop  870 1470 900 150 200
		sleep 3
		adb shell input draganddrop  897 2032 901 2040 200
		sleep 3

	fi


	echo "adb input tab"
	# adb shell input tap 914 1179

	if [ "$1" = "zhifubao" ]; then
		adb shell input draganddrop 866 652 950 658 200
	else
		adb shell input draganddrop  829 1296 922 1303 200
	fi
	sleep 22


	echo "adb input return"
	adb shell input keyevent 4
	sleep 3

	adb shell input keyevent 4
	sleep 3


done
