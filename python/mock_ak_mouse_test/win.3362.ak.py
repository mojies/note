# only using in python 2.x
# pip install pywin32
# pip install PyUserInput
# from pykeyboard import *
# from pymouse import *

# import win32api, win32con
# _m = PyMouse()
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
    "flowscreen": 0
}

_BASE_POS = [ 10, 174 ]

_PAGE = [
    [ 32, 200 ],       # Main Page
    [ 32, 287 ],       # Image setting
];

_P1_ACTION = [
    [ 149, 300 ],       # 360p 0
    [ 256, 300 ],       # 720p
    [ 373, 300 ],       # 1080p
    [ 150, 340 ],       # 2k

    [ 381, 381 ],       # switch  Frame mode 4

    [ 135, 440 ],       # FOV1 5
    [ 135, 495 ],       # FOV2
    [ 135, 555 ],       # FOV3
    [ 135, 618 ],       # Auto Frame
    [ 135, 666 ],       # Solo Frame

    [ 253, 480 ],       # R UP 10
    [ 281, 513 ],       # R RIGHT
    [ 219, 511 ],       # R LEFT
    [ 248, 549 ],       # R BOTTOM
    [ 170, 635 ],       # ZOOM 1x
    [ 340, 635 ],       # ZOOM 4x
    [ 249, 677 ],       # R RESET


    [ 367, 735 ],       # HDR 17
    [ 360, 780 ],       # Anti Flicker
    [ 150, 830 ],       # Anti Flicker 50Hz
    [ 250, 830 ],       # Anti Flicker 60Hz
];

RES_COUNT = 0



# ===========================================================================
def find_anker_window_pos():
    POS = pyautogui.locateOnScreen('win/DevicePage.png')
    # print( POS )
    return POS

def is_device_Page():
    pos = pyautogui.locateOnScreen('win/DevicePage.png')
    if pos == None:
        return False
    else:
        return True

def is_roulette_mode():
    pos = pyautogui.locateOnScreen('win/Roulette.png')
    if pos == None:
        return False
    else:
        return True

def is_HDR_enable():
    pos = pyautogui.locateOnScreen('win/HDR.png')
    if pos == None:
        return False
    else:
        return True

def is_anti_flicker_enable():
    pos = pyautogui.locateOnScreen('win/Flicker.png')
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
        time.sleep( 1 )

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


def func_test_flowscreen( ):
    global RES_COUNT
    STATISTICAL["flowscreen"] += 10

    func_skip_2_device_page()
    func_switch_frame_mode( 1 )

    for i in range(10):
        RES_COUNT += 1
        x = RES_COUNT%4
        pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
        time.sleep( 1.5 + random.random() )

        x = random.randint( 0, 100 )%7
        print( "Switch ROULETTE index: %d"%( x ) );
        x += 10

        if x >= 10 and x <= 13:
            for i in range( random.randint(1,10) ):
                pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
                time.sleep( 0.1 )
        elif x == 14 or x == 15 or x == 16:
            pos_x = _P1_ACTION[14][0] + int((_P1_ACTION[15][0]-_P1_ACTION[14][0])*random.random())
            pyautogui.click( AK_POS[0] + pos_x, AK_POS[1] + _P1_ACTION[14	][1] )
            time.sleep( 0.3 + 0.5*random.random() )
        else:
            pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )
            time.sleep( 0.3 + 0.5*random.random() )

_COUNT = 0
def func_test_switch_res_repeat():
    global _COUNT
    func_skip_2_device_page()

    _COUNT += 1
    x = 2 +  _COUNT%2
    print( "Switch resulotion index: %d"%( x ) );
    pyautogui.click( AK_POS[0] + _P1_ACTION[x][0], AK_POS[1] + _P1_ACTION[x][1] )

    s = random.random() * 60
    print( 'Sleep %d seconds'%( s ) )
    time.sleep( s )


# =====================================================================
POS = find_anker_window_pos();
if POS == None:
    print( "Didn't find Ankerwork APP" );
    exit(-1)
AK_POS[0] = POS.left - _BASE_POS[0]
AK_POS[1] = POS.top - _BASE_POS[1]


while True:
    stop_times = random.randint( 0, 10 )
    print( "LONG SLEEP AFTER: %d"%( stop_times ) );
    for i in range( stop_times ):
        print( "TEST TIMES: %d"%( i ) );

        # func_test_flowscreen()

        func_test_switch_res_repeat()

        # test_case = random.randint( 0, 100 )%2
        # if test_case == 0:
        #    test_times = random.randint( 1, 1 )
        #    func_switch_res( test_times )
        # elif test_case == 1:
        #     test_times = random.randint( 1, 20 )
        #     func_switch_fov( test_times )
        # elif test_case == 1:
        #    test_times = random.randint( 1, 1 )
        #    func_switch_roulette( test_times )
        # elif test_case == 3:
        #     test_times = random.randint( 0, 5 )
        #     func_switch_HDR( test_times )
        # elif test_case == 4:
        #     test_times = random.randint( 0, 9 )
        #     func_switch_anti_flicker( test_times )

    print( "STATISTICAL: ", STATISTICAL );
    time.sleep(1)
