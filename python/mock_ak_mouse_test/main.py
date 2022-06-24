# only using in python 2.x
# pip install pywin32
# pip install PyUserInput
# from pykeyboard import *
# from pymouse import *

# import win32api, win32con
# _m = PyMouse() #建立鼠标对象
# p1 = _m.position()
# print( p1 )

# ==============================================================================
# pip install pyautogui
import pyautogui
# pyautogui.position()

import random
import time

AK_POS = [0, 0]
STATISTICAL = {
    "res": 0,
    "fov": 0,
    "roulette": 0,
    "hdr": 0,
    "antiflicker": 0,
}

_PAGE = [
    [ 32, 200 ],       # Main Page
    [ 32, 287 ],       # Image setting
];

_P1_ACTION = [
    [ 149, 300 ],       # 360p
    [ 256, 300 ],       # 720p
    [ 373, 300 ],       # 1080p
    [ 150, 330 ],       # 2k

    [ 349, 376 ],       # switch  Frame mode

    [ 135, 440 ],       # FOV1
    [ 135, 495 ],       # FOV2
    [ 135, 555 ],       # FOV3
    [ 135, 618 ],       # Auto Frame
    [ 135, 666 ],       # Solo Frame

    [ 253, 480 ],       # R UP
    [ 281, 513 ],       # R RIGHT
    [ 219, 511 ],       # R LEFT
    [ 248, 549 ],       # R BOTTOM
    [ 146, 627 ],       # ZOOM 1x
    [ 337, 625 ],       # ZOOM 4x
    [ 249, 677 ],       # R RESET

    [ 367, 735 ],       # HDR
    [ 360, 780 ],       # Anti Flicker
    [ 150, 830 ],       # Anti Flicker 50Hz
    [ 250, 830 ],       # Anti Flicker 60Hz
];


# ===========================================================================
def find_anker_window_pos():
    POS = pyautogui.locateOnScreen('AKAPPMark.png')
    # print( POS )
    return POS

def is_device_Page():
    pos = pyautogui.locateOnScreen('DeivcePage.png')
    if pos == None:
        return False
    else:
        return True

def is_roulette_mode():
    pos = pyautogui.locateOnScreen('RouletteMode.png')
    if pos == None:
        return False
    else:
        return True

def is_HDR_enable():
    pos = pyautogui.locateOnScreen('HDRMode.png')
    if pos == None:
        return False
    else:
        return True

def is_anti_flicker_enable():
    pos = pyautogui.locateOnScreen('AntiFlickerMode.png')
    if pos == None:
        return False
    else:
        return True

# ===========================================================================
def func_skip_2_device_page():
    print( "AK_POS", AK_POS )
    print( "SWitch to device page" );
    if is_device_Page() == False:
        pyautogui.click( AK_POS[0] + _PAGE[0][0], AK_POS[1] + _PAGE[0][1])
        time.sleep( 0.2 )

def func_switch_frame_mode( mode ):
    if mode == 0:
        if is_roulette_mode() == False:
            return
    else:
        if is_roulette_mode() == True:
            return
    pyautogui.click( AK_POS[0] + _P1_ACTION[4][0], AK_POS[1] + _P1_ACTION[4][1])
    time.sleep( 0.3 )

# ===========================================================================
def func_switch_res( times ):
    STATISTICAL["res"] += times

    func_skip_2_device_page()

    for i in range( times ):
        x = random.randint( 0, 100 )%4
        print( "Switch resulotion index: %d"%( x ) );
        pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
        time.sleep( 2 )

def func_switch_fov( times ):
    STATISTICAL["fov"] += times

    func_skip_2_device_page()
    func_switch_frame_mode( 0 )

    for i in range( times ):
        x = random.randint( 0, 100 )%5
        print( "Switch FOV index: %d"%( x ) );
        x += 5
        pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
        time.sleep( 0.6 )

def func_switch_roulette( times ):
    STATISTICAL["roulette"] += times

    func_skip_2_device_page()
    func_switch_frame_mode( 1 )

    for i in range( times ):
        x = random.randint( 0, 100 )%7
        print( "Switch ROULETTE index: %d"%( x ) );
        x += 10
        pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
        time.sleep( 0.3 )

def func_switch_HDR( times ):
    STATISTICAL["hdr"] += times

    func_skip_2_device_page()

    for i in range( times ):
        x = 17
        print( "Switch HDR Mode " );
        pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
        time.sleep( 0.3 )


def func_switch_anti_flicker( times ):
    STATISTICAL["antiflicker"] += times

    func_skip_2_device_page()

    for i in range( times ):
        x = 18
        mode = random.randint( 0,3 )
        print( "Switch Anti-Flicker Mode: mode" );
        if mode == 0:
            if is_anti_flicker_enable() == False:
                continue
            pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
            time.sleep( 0.3 )
        elif mode == 1:
            if is_anti_flicker_enable() == False:
                pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
                time.sleep( 0.1 )
            x = 19
            pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
            time.sleep( 0.3 )

        elif mode == 2:
            if is_anti_flicker_enable() == False:
                pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
                time.sleep( 0.3 )
            x = 20
            pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
            time.sleep( 0.3 )


POS = find_anker_window_pos();
if POS == None:
    print( "Didn't find Ankerwork APP" );
    exit(-1)
AK_POS[0] = POS.left - 78
AK_POS[1] = POS.top - 22


while True:
    stop_times = random.randint( 0, 20 )
    print( "LONG SLEEP AFTER: %d"%( stop_times ) );
    for i in range( stop_times ):
        print( "TEST TIMES: %d"%( i ) );

        test_case = random.randint( 0, 100 )%5
        if test_case == 0:
            test_times = random.randint( 1, 10 )
            func_switch_res( test_times )
        elif test_case == 1:
            test_times = random.randint( 1, 20 )
            func_switch_fov( test_times )
        elif test_case == 2:
            test_times = random.randint( 1, 28 )
            func_switch_roulette( test_times )
        elif test_case == 3:
            test_times = random.randint( 0, 5 )
            func_switch_HDR( test_times )
        elif test_case == 4:
            test_times = random.randint( 0, 9 )
            func_switch_anti_flicker( test_times )

        print( "STATISTICAL: ", STATISTICAL );
    time.sleep(1)