# pip install pyautogui
import pyautogui
# pyautogui.position()

import random
import time
import os
import re
import cv2
import numpy as np

def f_imread_gray( path ):
    img_rgb = cv2.imread( path )
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    return img_gray

def f_get_screenshot():
    img = pyautogui.screenshot()
    img = np.array(img) 
    img = img[:, :, ::-1].copy()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img

# 615 310
# 1234 639
def f_get_answer_area():
    img = pyautogui.screenshot()
    img = np.array(img) 
    img = img[ 310:639, 586:1300, ::-1].copy()
    # img = img[ 310:639, 586:1181, ::-1].copy()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # cv2.imshow( 'aa', img )
    return img
# f_get_answer_area()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit(0)
    
def f_conv_aa2full_pos( pos ):
    ret = ( pos[0] + 586, pos[1]+310 )
    print( "ret -> ", ret )
    return ret

def f_find_tmlp( parent, child ):
    res = cv2.matchTemplate( parent, child, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.9)
    if len(loc[0]) == 1:
        return ( loc[1][0], loc[0][0] )
    else:
        return None


def f_enter_start():
    screen = f_get_screenshot()
    start = f_imread_gray( 'start.png' )
    p_start = f_find_tmlp( screen, start )
    if p_start == None:
        return 
    pyautogui.click( p_start[0], p_start[1] )
    # pyautogui.click( 1003, 941 )
    time.sleep(0.8)

# img = f_get_screenshot()
# tplt = f_imread_gray('child.png')
# w, h = tplt.shape[::-1]
# res = cv2.matchTemplate( img, tplt, cv2.TM_CCOEFF_NORMED)
# loc = np.where(res >= 0.9)
# img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# print(loc)
# pt1 = (loc[1][0], loc[0][0])
# rec = (int(loc[1] + w), int(loc[0] + h))
# cv2.rectangle( img_rgb, pt1, rec, (255,0,0), 2)
# img = img_rgb

# print(loc)
# img = pyautogui.screenshot()
# img = np.array(img) 
# Convert RGB to BGR 
# img = img[:, :, ::-1].copy()
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# child = f_imread_gray('child.png')

# img = cv2.imread('child.png')
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# cv2.imshow( 'test', img )
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit(0)


# {
#     "1":{
#         Q: [],
#         A: []
#     }
# }
ans_f = {}
yes_tmpl = f_imread_gray( 'yes.png' )

for (dirpath, dirnames, filenames) in os.walk( './' ):
    for f in filenames:
        f_find = re.findall('^(\d+)\.png', f)
        if len( f_find ) == 1:
            k = f_find[0]
            ans_f[ k ] = {
                "Q": f_imread_gray( f ),
                "A": [],
            }

    for f in filenames:
        f_find = re.findall('^(\d+)\.(\d+)\.png', f)
        if len( f_find ) == 1:
            ans_f[ f_find[0][0] ]["A"].append( f_imread_gray( f ) )

f_enter_start()

while True:
    p_a = None
    # screen = f_get_screenshot()
    screen = f_get_answer_area()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for key in ans_f.keys():
        # p_q = pyautogui.locateOnScreen(key + '.png')
        p_q = f_find_tmlp( screen, ans_f[ key ]["Q"] )
        if p_q == None: 
            continue
        else:
            print( "%s -> %d, %d"%( key, p_q[0], p_q[1] ) )
            p_a = ans_f[ key ]["A"]
            break
    if p_a == None:
        break
    finded = False
    for ans in p_a:
        # p = pyautogui.locateOnScreen( ans )
        # pyautogui.click( p.left, p.top )
        p = f_find_tmlp( screen, ans )
        print( p )
        if p != None:
            pyautogui.click( f_conv_aa2full_pos( (p[0], p[1]) ) )
            finded = True
    if finded:
        pyautogui.click(1075, 948 )
        # p = f_find_tmlp( screen, yes_tmpl )
        # pyautogui.click( p[0], p[1] )
    time.sleep(0.2)
