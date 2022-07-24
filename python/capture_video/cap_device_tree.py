# page 0 code
# page 2 website chomre
# page 3 OBS
# page 4 preview
# ==============================================================================
# pip install pyautogui
import pyautogui as ag
# pyautogui.position()

import random
import time

G_PAGE = [
    # page0
    [ 50, 10 ],
    # page1
    [ 100, 10 ],
    # page2
    [ 150, 10 ],
    # page3
    [ 184, 10 ],
]

G_POS = [
    # page0
    [ 50, 10 ],
    # page1
    [ 100, 10 ],
    # page2
    [ 150, 10 ],

    # chrome addresss
    [ 300, 100 ],

    # play position
    [ 966, 465 ],

    # zero progress
    [ 353, 690 ],

    # show control bar
    [ 470, 730 ],

    # full screen
    [ 1520, 715 ]

]

G_RECORD_ADDRESS = [
    # "https://www.100ask.net/detail/v_5e61ad734df9d_mq11w8T9/3",
    # 1.2_字符设备驱动的传统写法
    # 1.3_字符设备驱动的编译测试
    # 1.4_总线设备驱动模型
    # 1.5_使用设备树时对应的驱动编程
    # 1.6_只想使用设备树不想深入研究怎么办
    # 2.1_DTS格式
    # 2.2_DTB格式
    # "https://www.100ask.net/detail/v_5e61ad6d1a0fc_V6RCUL5I/3",
    # "https://www.100ask.net/detail/v_5e61ad674052b_TzQmZuTi/3",
    # "https://www.100ask.net/detail/v_5e61ad5f995f2_tGKWPxE7/3",
    # "https://www.100ask.net/detail/v_5e61ad57c4de8_Y8afdk3v/3",
    # "https://www.100ask.net/detail/v_5e61aca77e541_airDRsFB/3",
    # "https://www.100ask.net/detail/v_5e61aec2f3ae2_E5SqlkRt/3",
    # "https://www.100ask.net/detail/v_5e61ae1f585ea_eKEP8yMK/3",

    # 3.1_从源头分析_内核head.S对dtb的简单处理
    # 3.2_对设备树中平台信息的处理(选择machine_desc)
    # 3.3_对设备树中运行时配置信息的处理
    # 3.4_dtb转换为device_node(unflatten)
    # 3.5_device_node转换为platform_device
    # 3.6_platform_device跟platform_driver的匹配
    # 3.7_内核中设备树的操作函数
    # 3.8_在根文件系统中查看设备树
    # "https://www.100ask.net/detail/v_5e61aefa741b1_EGz7MnKS/3",
    # "https://www.100ask.net/detail/v_5e61aef86477c_Yz1CloAQ/3",
    # "https://www.100ask.net/detail/v_5e61aef600fdf_B4PlOBHr/3",
    # "https://www.100ask.net/detail/v_5e61aef3daea3_ICKHomw6/3",
    # "https://www.100ask.net/detail/v_5e61aef15519f_EKXpcE1c/3",
    # "https://www.100ask.net/detail/v_5e61aed2dd733_GMn5Dgh5/3",
    # "https://www.100ask.net/detail/v_5e61aecd22f12_MCcCfbqg/3",
    # "https://www.100ask.net/detail/v_5e61aec8ec529_PbxMzKoV/3",

    # 4.1_传递dtb给内核
    # 4.2_dtb的修改原理
    # 4.3_dtb的修改命令fdt移植
    # "https://www.100ask.net/detail/v_5e61b2bfcd048_EsRzhEhu/3",
    # "https://www.100ask.net/detail/v_5e61b2b9e8e8d_AfarYeI9/3",
    # "https://www.100ask.net/detail/v_5e61b2b5aea09_ivcZOAWE/3",

    # 5.1_中断概念的引入与处理流程
    # 5.2_Linux对中断处理的框架及代码流程简述
    # 5.3_中断号的演变与irq_domain
    # 5.4_示例_在S3C2440上使用设备树描述中断体验
    # 5.5_示例_使用设备树描述按键中断
    # 5.6_内核对设备树中断信息的处理过程
    # "https://www.100ask.net/detail/v_5e61b2dc4d45d_MrupX5pK/3",
    # "https://www.100ask.net/detail/v_5e61b2d767721_LWUn7RUj/3",
    # "https://www.100ask.net/detail/v_5e61b2d397032_HVqC1twF/3",
    # "https://www.100ask.net/detail/v_5e61b2ce01a89_VqmcGod2/3",
    # "https://www.100ask.net/detail/v_5e61b2c983b3f_FH9L0L0o/3",
    # "https://www.100ask.net/detail/v_5e61b2c429e32_Iq0ImOaL/3",


    # 6.1_使用设备树给DM9000网卡_触摸屏指定中断
    # 6.2_在设备树中时钟的简单使用
    # 6.3_在设备树中pinctrl的简单使用
    # 6.4_使用设备树给LCD指定各种参数
    # "https://www.100ask.net/detail/v_5e61b3be7c6dc_uEtA1xTR/3",
    # "https://www.100ask.net/detail/v_5e61b3b9661d8_vkdew60I/3",
    # "https://www.100ask.net/detail/v_5e61b3b4b4c81_wVAk5zA9/3",
    # "https://www.100ask.net/detail/v_5e61b3afa79a1_VVVETLMF/3",
]

def click_pos( num ):
    pos = num
    ag.click( G_POS[ pos ][0], G_POS[ pos ][1] )
    time.sleep(0.2)

def moveto( num ):
    pos = num
    ag.moveTo( G_POS[ pos ][0], G_POS[ pos ][1] )
    time.sleep(0.2)

def input_txt( s ):
    l_str = list( s )
    for i in range( len(l_str) ):
        ag.press( l_str[i] )
        time.sleep(0.03)

def input_enter():
    ag.press( 'enter' )
    time.sleep(0.5)

def skip_page( num ):
    if num < 0:
        num = 0
    if num > 3:
        num = 3

    pos = num
    ag.click( G_PAGE[ pos ][0], G_PAGE[ pos ][1] )
    time.sleep(0.2)

def skip_chrome_address():
    click_pos( 3 )

def click_play():
    click_pos( 4 )

def switch_2_zero_progress():
    moveto( 5 )
    time.sleep(1)
    click_pos( 5 )

def is_playing():
    pos = ag.locateOnScreen('img/play.icon.png')
    if pos == None:
        return False
    else:
        return True

def is_zero_progress():
    pos = ag.locateOnScreen('img/zero.flag.png')
    if pos == None:
        return False
    else:
        return True

def is_play_ended():
    pos = ag.locateOnScreen('img/play_end3.png')
    if pos == None:
        return False
    else:
        return True

def get_start_record_pos():
    return ag.locateOnScreen('img/start.recording.png')
def get_stop_record_pos():
    return ag.locateOnScreen('img/stop.recording.png')

def chrome_into_address( addr ):
    skip_page(2)

    skip_chrome_address()
    # with ag.hold('ctrl'):
    #     ag.press( A  )
    ag.keyDown( 'ctrl' )
    ag.press( 'a' )
    ag.keyUp( 'ctrl' )
    time.sleep(0.1)
    input_txt( addr )
    ag.press( 'enter' )
    time.sleep( 20 )

def chrome_100ask_play_frome_zero():
    click_play()
    ag.moveTo( G_POS[6][0], G_POS[6][1] )
    time.sleep(2)
    if is_zero_progress():
        return;
    else:
        switch_2_zero_progress()
    time.sleep(1)
    click_pos( 7 )

def wait_play_end():
    while True:
        if is_play_ended():
            break
        time.sleep(10)

def start_record():
    with ag.hold('win'):
        with ag.hold('shift'):
            time.sleep(0.1)
            ag.keyDown( 'r' )
            ag.keyUp( 'r' )
            time.sleep(0.1)

    # skip_page( 3 )
    # time.sleep(2)
    # while True:
    #     pos = get_start_record_pos()
    #     if pos == None:
    #         print( "--------------------> start record get buttom: ", pos )
    #         time.sleep(3)
    #     else:
    #         break
    # time.sleep(0.1)
    # ag.click( pos.left, pos.top )

def stop_record():
    with ag.hold('win'):
        with ag.hold('shift'):
            time.sleep(0.1)
            ag.keyDown( 's' )
            ag.keyUp( 's' )
            time.sleep(0.1)

    # skip_page( 3 )
    # time.sleep(2)
    # pos = get_stop_record_pos()
    # if pos == None:
    #     print( "--------------------> stop record get buttom: ", pos )
    #     exit(-1)
    # time.sleep(0.1)
    # ag.click( pos.left, pos.top )
    # time.sleep(1)


def record_video(addr):
    chrome_into_address( addr )
    chrome_100ask_play_frome_zero()
    time.sleep(0.3)
    print( "--------------------> start recording" )
    start_record()
    wait_play_end()
    print( "--------------------> stop recording" )
    stop_record()
    ag.press( 'esc' )

for i in range( len(G_RECORD_ADDRESS) ):
    print( "--------------------> start playing" )
    record_video( G_RECORD_ADDRESS[ i ] )
    time.sleep(30)

