# pip install pyautogui
import pyautogui
screen_szie = pyautogui.size()
# pyautogui.position()
import random
import time
import os
import re
import numpy as np
import cv2

import easyocr



# reader = easyocr.Reader(['ch_sim','en']) 
# reader = easyocr.Reader(['en']) 
# result = reader.readtext('t1.png')
# print( result )

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

def f_find_tmlp( parent, child ):
    res = cv2.matchTemplate( parent, child, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.9)
    if len(loc[0]) == 1:
        return ( loc[1][0], loc[0][0] )
    else:
        return None

def f_ocr_get_int_in_gray_img( ocrer, img, pos, size ):
    img = img[ pos[1]:pos[1]+size[1], pos[0]:pos[0]+size[0]].copy()

    img = cv2.pyrUp( img )
    img = cv2.pyrUp( img )
    _, img = cv2.threshold( img, 200, 255, 0 )
    # img = cv2.blur(img, (3,3))


    # 腐蚀
    # kernel = np.ones((2,2),np.uint8)
    # img = cv2.erode( img, kernel,iterations = 2)

    # 膨胀
    # kernel = np.ones((3,3),np.uint8)
    # img = cv2.dilate(img, kernel, iterations = 1)

    ocr_res = ocrer.readtext( img, allowlist="0123456789", text_threshold=0.5 )

    cv2.imshow('a', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print( ocr_res )
    

# 1. get start time
def f_get_start_time_list( ocrer ):
    # 1. 定位 stary 坐标
    screen_img = f_get_screenshot()

    print( "pyautogui.size()-> ", screen_szie )
    print( "screen_img shape -> ", screen_img.shape )
    
    start_img = f_imread_gray( 'start.png' )
    start_pos = f_find_tmlp( screen_img, start_img )
    if start_pos == None:
        return
    print( "start_pos -> ", start_pos )
    (s_w, s_h) = start_pos

    # 2. 裁剪出 start 列
    # 1353 - 1234
    t1 = 1234
    t2 = 1353
    h_size = screen_szie[1]
    
    start_col_img = screen_img[ s_h:h_size, s_w: s_w+t2-t1].copy()
    cv2.imshow('a', start_col_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 3. 文字识别
    ocr_res = ocrer.readtext( start_col_img )
    print( ocr_res )
    # [
    #   ([[3, 5], [79, 5], [79, 23], [3, 23]], '0#aitIa', 0.0727048983320107),
    #   ([[5, 89], [77, 89], [77, 105], [5, 105]], '2022/09/01', 0.999090953650257) ... ]

    # 4. 日期转换
    real_res = []
    for tmp in ocr_res:
        if tmp[2] > 0.8:
            real_res.append( tmp )
    print( real_res )
    # 生成 cost 日期坐标 real_res.pos + ( 230, 0 )
    # width 75
    # hight 30
    cost_pos = []
    for tmp in real_res:
        cost_pos.append( [ np.array(tmp[0][0]) + start_pos - (8,10) + (230, 0), ( 150, 34 ) ] )
    print( "cost_pos -> ", cost_pos )

    # 5. 获取对应位置耗时图片
    for tmp in cost_pos:
        f_ocr_get_int_in_gray_img( ocrer, screen_img, tmp[0], tmp[1]  )
    # 6. 识别耗时图片位置文字
    # 7. 计算结束时间
    # 8. 自动填充结束时间
    
    
ocrer = easyocr.Reader(['ru', 'en']) 
f_get_start_time_list( ocrer )