#!/bin/bash


while true
do
	echo "adb input tab"
	# adb shell input tap 914 1179
	adb shell input draganddrop  829 1296 922 1303 200
	sleep 22

	echo "adb input return"
	adb shell input keyevent 4
	sleep 3

	adb shell input keyevent 4
	sleep 3

	adb shell input draganddrop  870 1470 900 150 200
	sleep 3

	adb shell input draganddrop  897 2032 901 2040 200
	sleep 3

done
