# for(var ii = 0; ii < b.length; ii++){ if(b[ii].href.match('100ask')){ cc = b[ii].href.match('/(v_.*)/'); if(cc && cc.length > 2) console.log( cc[2] ) } }
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

# a = document.getElementsByClassName('class-dec');for(var i=0;i<a.length;i++){console.log(a[i].innerText )}
G_RECORD_ADDRESS = [
    # 1.1-工具_使用AndroidStudio来阅读源码
    # 1.2-工具_建模工具bouml
    # 1.3-工具_使用bouml制作时序图
    # "v_5e901505e0afa_KJSFzhN2",
    # "v_5e9014d9a34ea_bQkzvN0C",
    # "v_5e9014b57fbf7_q8dgwzr8",

    # 2.1.1_编写第1个Android应用程序实现按钮和复选框
    # 2.1.2_让Android应用程序访问C库
    # 2.1.3_Android程序操作LED
    # 2.2.1_Android硬件访问服务框架
    # 2.2.2_Android硬件访问服务编写系统代码
    # 2.2.3_Android硬件访问服务编写APP代码
    # 2.2.4_Android硬件访问服务编写HAL代码
    # 2.2.5_Android硬件访问服务使用反射

    # "v_5e90165ae081a_ReYLdIX2",
    # "v_5e901637d67c2_Bp8GFu1c",
    # "v_5e901610d8f51_6Uq51oJq",
    # "v_5e9015e3bd856_KzKqXd52",
    # "v_5e9015b619e31_Naa37Jzr",
    # "v_5e9015981c06d_vTtO90Hw",
    # "v_5e901578dfeca_wckxanC4",
    # "v_5e90155606055_ULLt2ya5",

    # 3.1_基础知识Android消息处理机制
    # 3.2_基础知识ArrayMap
    # "v_5e9018109ae15_C5wLFSz0",
    # "v_5e9017ff0b460_zrPxZ0uU",

    # 4.1_Android灯光系统_总体框架
    # 4.2_Android灯光系统_led_class驱动
    # 4.3_Android灯光系统_编写HAL_lights.c
    # 4.4_Android灯光系统_源码分析_电池灯
    # 4.5_Android灯光系统_源码分析_通知灯
    # 4.6_Android灯光系统_源码分析_背光灯
    # "v_5e9018cc59a65_SIfcAl2d",
    # "v_5e9018bcbd9e8_6bxLvjCV",
    # "v_5e9018ad53063_aw6hZgPs",
    # "v_5e90189c7ac74_2HAIhUl1",
    # "v_5e90188beee2e_LhnompgO",
    # "v_5e901873aebe0_d5lFQDy7",

    # 5.1.1_Binder系统_C程序示例_框架分析
    # 5.1.2_Binder系统_C程序示例_编写程序
    # 5.1.3_Binder系统_C程序示例_编译查错
    # 5.1.4_Binder系统_C程序示例_测试与总结
    # 5.2.1_Binder系统_驱动情景分析_数据结构
    # 5.2.2_Binder系统_驱动情景分析_打印数据交互过程
    # 5.2.3_Binder系统_驱动情景分析_服务注册过程_概述
    # 5.2.4_Binder系统_驱动情景分析_服务注册过程_分析
    # 5.2.5_Binder系统_驱动情景分析_服务获取过程
    # 5.2.6_Binder系统_驱动情景分析_服务使用过程
    # 5.2.7_Binder系统_transaction_stack机制_REPLY
    # 5.2.8_Binder系统_transaction_stack机制_双向服务
    # 5.2.9_Binder系统_server的多线程实现
    # 5.3.1_Binder系统_c++实现_编写程序
    # 5.3.2_Binder系统_c++实现_编译测试
    # 5.3.3_Binder系统_c++实现_内部机制_回顾关键点
    # 5.3.4_Binder系统_c++实现_内部机制_代理类BpXXX分析
    # 5.3.5_Binder系统_c++实现_内部机制_数据传输
    # 5.3.6_Binder系统_c++实现_内部机制_添加服务
    # 5.4.1_Binder系统_c++实现_编写程序
    # 5.4.2_Binder系统_JAVA实现_hello服务_编程
    # 5.4.3_Binder系统_JAVA实现_hello服务_测试
    # 5.4.4_Binder系统_分层
    # 5.4.5_Binder系统_JAVA实现_内部机制_Client端
    # 5.4.6_Binder系统_JAVA实现_内部机制_Server端
    # 5.4.7_回看SystemServer_硬件访问服务及课后作业
    # "v_5e93bcfb27e53_50Ky7VJI",
    # "v_5e93bce22d935_1uyEoFYF",
    # "v_5e93bcc92a129_2HLDSIuQ",
    # "v_5e93bca48951a_CR3qshTa",
    # "v_5e93bc844a4d3_4ACzUb8K",
    # "v_5e93bc6cb5afd_Yeb1qfSO",
    # "v_5e93bc5603498_D3Whi22R",
    # "v_5e93bc437e78e_EgNV2o2p",
    # "v_5e93bc1c0f4d3_Al50Hz8H",
    # "v_5e93bc07b7e9a_qH3KiwyO",
    # "v_5e93bbf02b2c0_HbJtmWEV",
    # "v_5e93bbb21e379_0sThTswZ",
    # "v_61d53ed5e4b07ecd8e205682",
    # "v_5e93bb405c5e9_omUMiTf6",
    # "v_5e93bb2543fbf_vxqSA9dT",
    # "v_5e93bb10aaec5_uAmyXq3L",
    # "v_5e93babed04aa_rLxWAr6I",
    # "v_5e93ba94d4100_9P06Nd2q",
    # "v_5e93ba7390ea5_64FdSkl8",
    # "v_5e93ba382daf5_HHWwNQkH",
    # "v_5e93ba1a0ae0c_ginMqi9o",
    # "v_5e93ba0134b99_m3OdWkVN",
    # "v_5e93b9d836964_FbXmXohB",
    # "v_5e93b9b9d7d6e_ALoRVsNa",
    # "v_5e93b99bf2c3d_Tbww9vUO",
    # "v_5e93b97a710e5_rtTZej8y",

    # 6.1_ALSA声卡_裸板之原理和框架
    # 6.2_ALSA声卡_裸板之编写程序
    # 6.3_ALSA声卡_裸板之编译和测试
    # 6.4_ALSA声卡_ALSA驱动框
    # 6.5_ALSA声卡_ASoC驱动框架
    # 6.6_ALSA声卡_体验声卡
    # 6.7_ALSA声卡_分析调用过程
    # 6.8_ALSA声卡_从零编写之框架
    # 6.9_ALSA声卡_从零编写之参数设置
    # 6.10_ALSA声卡_从零编写之数据传
    # 6.11_ALSA声卡_从零编写之调试
    # 6.12_ALSA声卡_从零编写之添加音量控制
    # 6.13_ALSA声卡_从零编写之WM8976
    # 6.14_ALSA声卡_移植原厂WM8976驱动
    # 6.15_ALSA声卡_修改内核声卡BUG
    # 6.16_ALSA声卡编写_ALSA声卡应用程序
    # "v_5e6a0b9d3c332_8pH24d8W",
    # "v_5e6a0b9b6789c_Ii7Ju8vH",
    # "v_5e6a0b9958d9d_dz5n4NbD",
    # "v_5e6a0b9704d5d_pc37lKOZ",
    # "v_5e6a0b95213da_mCCgcVp8",
    # "v_5e6a0b9392809_oh5SQGPV",
    # "v_5e6a0b91b22df_mr4baA5r",
    # "v_5e6a0b8ff3f15_QaXWNPeb",
    # "v_5e6a0b8e143d4_k0LbsQj9",
    # "v_5e6a0b8c23d3c_Yk7AiVAC",
    "v_5e6a0b8a4b333_zlwAKxQR",
    "v_5e6a0b88a020b_YEB2aepP",
    "v_5e6a0b86036ec_yDgD8S6u",
    "v_5e6a0b82cc1e6_TSOp6TvD",
    "v_5e6a0b8109210_Y7hHgDS4",
    "v_5e6a0b7e32d7a_cvicAZQx",


    # 7.1_声音的采集与存储
    # 7.2_Android音频系统框架简述
    # 7.3.1_Linux音频驱动_alsa音频驱动框架
    # 7.3.2_Linux音频驱动_ASoC音频驱动框架
    # 7.3.3_Linux音频驱动_tiny4412声卡驱动移植_combine
    # 7.3.4_Linux音频驱动_声卡控制之kcontrol
    # 7.3.5_Linux音频驱动_DAPM_widget_route_path
    # 7.3.6_Linux音频驱动_DAPM的kcontrol注册过程
    # 7.3.7_Linux音频驱动_route_path添加过程分析
    # 7.3.8_Linux音频驱动_DAPM的情景分析_构造过程
    # 7.3.9_Linux音频驱动_DAPM的情景分析_使用过程
    # 7.3.10_Linux音频驱动_tiny4412声卡驱动录音功能调试
    # 7.4.1_Android音频_分析思路
    # 7.4.2_Android音频_以例子说明几个重要概念
    # 7.4.3_Android音频_所涉及文件形象讲解
    # 7.4.4_Android音频_AudioPolicyService启动过程分析
    # 7.4.5_Android音频_AudioFlinger启动过程分析
    # 7.4.6_Android音频_AudioTrack创建过程
    # 7.4.7_Android音频_AudioPolicyManager堪误与回顾
    # 7.4.8_Android音频_AudioTrack创建过程_选择output
    # 7.4.9_Android音频_AudioTrack创建过程_Track和共享内存
    # 7.4.10_Android音频_音频数据的传递
    # 7.4.11_Android音频_PlaybackThread处理流程
    # 7.5.1_项目实战1_耳麦拔插_驱动程序上报耳麦拔插事件
    # 7.5.2_项目实战1_耳麦拔插_在状态栏显示耳麦图标
    # 7.5.3_项目实战1_耳麦拔插_耳麦拔插事件调用流程分析
    # 7.5.4_项目实战1_耳麦拔插_切换声音通道流程
    # 7.6.1_音频系统HAL分析_HAL之框架
    # 7.6.2_音频系统HAL分析_HAL之调用流程源码分析
    # 7.7.1_音量调节_音量相关概念
    # 7.7.2_音量调节_AudioFlinger层调节音量流程
    # 7.7.3_音量调节_音量键和Setting界面调节音量流程
    # 7.8.1_项目实战2_多APP同时录音_使用c++编写录音程序
    # 7.8.2_项目实战2_多APP同时录音_录音框架及代码流程
    # 7.8.3_项目实战2_多APP同时录音_修改代码支持多APP同时录音

    "v_5e69ef411071d_gSCpjJxv",
    "v_5e69ef3c70579_v7qF8EDJ",
    "v_5e69ef3806ea4_NwBd55jT",
    "v_5e69ef339fae5_wMmPRwhE",
    "v_5e69ef2f3f563_hkc3Rkwu",
    "v_5e69ef2a8157d_Vx3MUu1O",
    "v_5e69ef250c4e5_hOFyuLTs",
    "v_5e69ef1fb9964_BOGLmi45",
    "v_5e69ef1a4bd50_gZkjgPwG",
    "v_5e69ef1532e05_on0O9GoJ",
    "v_5e69ef0f6c707_P4vvaz3G",
    "v_5e69eef7bd413_7onEVn7D",
    "v_5e69eaf9242db_Dxu12fKc",
    "v_5e69eaf32b738_wJiaYwII",
    "v_5e69eae53e13e_hlvjwJP7",
    "v_5e69eadeee1c5_BpWHuctL",
    "v_5e69eada948f3_4bVrW5sq",
    "v_5e69ead5f3121_B8Fwi4lP",
    "v_5e69eaceb6504_aI7EiALw",
    "v_5e69eaca1c6e5_DEud5V6Z",
    "v_5e69eac5af38b_9Te5wWcN",
    "v_5e69ea46823fe_VdI7OlxW",
    "v_5e69ea3f4c33a_hwbL1l9k",
    "v_5e69e887937e8_P5uYDasr",

    "v_5e69e87984f53_KCzr6t2w",
    "v_5e69e86272a66_p23C28G2",
    "v_5e69e76f109e7_DeToZzuO",
    "v_5e69e73ee509e_jDRj13iu",
    "v_5e69e72f6ed24_5PPXcYQ6",
    "v_5e69e6fe45930_HuV7O3tD",
    "v_5e69e6f1db7c6_8avRhiTE",
    "v_5e69e6e3e0242_G7neu6px",
    "v_5e69e6ae93bfd_EYOqvLb0",
    "v_5e69e698ef861_bMrQJiV4",
    "v_5e69e5e2603a3_vkRVSlSA",

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
    time.sleep( 10 )

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
    record_video( "https://www.100ask.net/detail/" + G_RECORD_ADDRESS[ i ] + "/3" )
    time.sleep(30)

