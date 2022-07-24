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
    "https://www.100ask.net/detail/v_609a0102e4b0adb2d8630c56/3",
    "https://www.100ask.net/detail/v_609e15e7e4b0adb2d864200f/3",
    "https://www.100ask.net/detail/v_60a7bbc1e4b00176519dc0fc/3",
    "https://www.100ask.net/detail/v_60a8573ae4b0f120ffbfe421/3",
    "https://www.100ask.net/detail/v_60b46a17e4b0c726421aa000/3",
    "https://www.100ask.net/detail/v_60b46a50e4b0017651a07174/3",
    "https://www.100ask.net/detail/v_60bae127e4b0f120ffc45a22/3",
    "https://www.100ask.net/detail/v_60bae15de4b0017651a22f94/3",
    "https://www.100ask.net/detail/v_60c8ea08e4b0017651a54028/3",
    "https://www.100ask.net/detail/v_60c8ea37e4b0f120ffc76c6a/3",
    "https://www.100ask.net/detail/v_60d0488fe4b0f120ffc914e0/3",
    "https://www.100ask.net/detail/v_60d9af10e4b057a4e728d2d6/3",
    "https://www.100ask.net/detail/v_60dd1ab9e4b08aeb71e151b6/3",
    "https://www.100ask.net/detail/v_60e2712ee4b0876c0c22060b/3",
    "https://www.100ask.net/detail/v_60e59488e4b0bd401d893f31/3",
    "https://www.100ask.net/detail/v_60e64974e4b0b2c421424820/3",
    "https://www.100ask.net/detail/v_60f3c39ce4b0041622bd8976/3",
    # "https://www.100ask.net/detail/v_60f4d062e4b0041622bdad8c/3",
    # "https://www.100ask.net/detail/v_60fbcc3be4b0ab00e332a9ae/3",
    # "https://www.100ask.net/detail/v_61077e0ae4b0a27d0e384ade/3",
    # "https://www.100ask.net/detail/v_61077e2ee4b054ed7c48e285/3",
    # "https://www.100ask.net/detail/v_61107c50e4b0cce271bb551c/3",
    # "https://www.100ask.net/detail/v_61107c76e4b0bf6430033d59/3",
    # "https://www.100ask.net/detail/v_6119d2a7e4b0cce271be6a2e/3",
    # "https://www.100ask.net/detail/v_6119d2cfe4b0cce271be6a5c/3",
    # "https://www.100ask.net/detail/v_612c76b4e4b0adcd5a9d3bde/3",
    # "https://www.100ask.net/detail/v_61356325e4b0448bf655dc71/3",
    # "https://www.100ask.net/detail/v_6135634de4b04518c61088f7/3",
    # "https://www.100ask.net/detail/v_613eeccee4b0dfaf7fa31d55/3",
    # "https://www.100ask.net/detail/v_613eed09e4b0dfaf7fa31d8d/3",
    # "https://www.100ask.net/detail/v_613eed41e4b0dfaf7fa31db8/3",
    # "https://www.100ask.net/detail/v_616d090fe4b05adf20761265/3",
    # "https://www.100ask.net/detail/v_616fa3f4e4b0cf90f9bb9819/3",
    # "https://www.100ask.net/detail/v_61762f0ce4b03b86217ca501/3",
    # "https://www.100ask.net/detail/v_61762f0ee4b0740575ad49b8/3",
    # "https://www.100ask.net/detail/v_61762f0de4b0ed214bb6965a/3",
    # "https://www.100ask.net/detail/v_6191f247e4b0bab3cb7bd52e/3",
    # "https://www.100ask.net/detail/v_6191f267e4b077a2b360b6bc/3",
    # "https://www.100ask.net/detail/v_619b2a94e4b09b5fe0b4b51d/3",
    # "https://www.100ask.net/detail/v_61a311f1e4b0b4bf0ab32a97/3",
    # "https://www.100ask.net/detail/v_61d336aae4b07ecd8e1fca39/3",
    # "https://www.100ask.net/detail/v_61dbd517e4b07ecd8e21ffee/3",
    # "https://www.100ask.net/detail/v_61dbd573e4b07ecd8e220034/3",
    # "https://www.100ask.net/detail/v_61eef1d6e4b054255d99b616/3",
    # "https://www.100ask.net/detail/v_620a2dede4b02b82584aa87e/3",
    # "https://www.100ask.net/detail/v_620a2e22e4b0beaee429fa18/3",
    # "https://www.100ask.net/detail/v_621ced0fe4b054255da2b61d/3",
    # "https://www.100ask.net/detail/v_623936e2e4b0f7cb7c74fc3b/3",
    # "https://www.100ask.net/detail/v_6239378ce4b09dda12507ee0/3",
    # "https://www.100ask.net/detail/v_62c2574be4b0a51feefacb61/3",

    # 3.1 性能分析专题_课程介绍
    # 3.2 性能分析专题_下载Android原生源码
    # 3.3 性能分析专题_编译Android模拟器
    # 3.4 性能分析专题_在Android模拟器中如何替换库和img
    # 3.5 性能分析专题_如何抓取systrace
    # 3.6 性能分析专题_如何通过perfetto抓取trace
    # 3.7 性能分析专题_systrace基本操作
    # 3.8 性能分析专题_perfetto基本操作
    # 3.9 性能分析专题_在Camera App或Java Framework添加trace
    # 3.10 性能分析专题_在Camera Native Framework添加trace
    # 3.12 Android_Camera_性能分析专题_Camera启动性能拆解
    # 3.11 性能分析专题_Camera软件栈介绍
    # 3.13 从Camera App和Java Framework角度详解Camera启动性能
    # 3.14 从CameraServer角度详解Camera启动性能
    # 3.15 SwitchCamera性能分析
    # "https://www.100ask.net/detail/v_627b1acde4b01c509aaea519/3",
    # "https://www.100ask.net/detail/v_627b1b1fe4b09dda12668b54/3",
    # "https://www.100ask.net/detail/v_627b1bece4b01c509aaea5ec/3",
    # "https://www.100ask.net/detail/v_627b1c6de4b01a4851fd3c7f/3",
    # "https://www.100ask.net/detail/v_627b1cc0e4b09dda12668c40/3",
    # "https://www.100ask.net/detail/v_627b1d07e4b09dda12668c74/3",
    # "https://www.100ask.net/detail/v_627b1d88e4b0cedf38b01d3b/3",
    # "https://www.100ask.net/detail/v_627b1dd5e4b0812e1797cf65/3",
    # "https://www.100ask.net/detail/v_627b1e48e4b01c509aaea7ef/3",
    # "https://www.100ask.net/detail/v_627b1f27e4b01c509aaea88e/3",
    # "https://www.100ask.net/detail/v_628b3af0e4b09dda126c123a/3",
    # "https://www.100ask.net/detail/v_6281b395e4b01a4851ff6805/3",
    # "https://www.100ask.net/detail/v_628b3b2ee4b01a485202ba41/3",
    # "https://www.100ask.net/detail/v_6294664ae4b0cedf38b886d8/3",
    # "https://www.100ask.net/detail/v_62a6d64be4b09dda12751e9f/3",
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
    # into console
    # ag.press( 'F12' )
    # time.sleep( 3 )
    # click_pos( 5 )
    # input_txt( 'a = document.getElementById("vjs_video_3")' )
    # input_enter()
    # input_txt( 'a.id = "vjs_video_4' )
    click_play()
    ag.moveTo( G_POS[6][0], G_POS[6][1] )
    time.sleep(3)
    if is_zero_progress():
        return;
    else:
        switch_2_zero_progress()
    time.sleep(1)
    click_pos( 7 )

def wait_play_end():
    while True:
        if is_play_ended():
            ag.press( 'esc' )
            break
        time.sleep(10)

def start_record():
    skip_page( 3 )
    time.sleep(2)
    while True:
        pos = get_start_record_pos()
        if pos == None:
            print( "--------------------> start record get buttom: ", pos )
            time.sleep(3)
        else:
            break
    time.sleep(0.1)
    ag.click( pos.left, pos.top )

def stop_record():
    skip_page( 3 )
    time.sleep(2)
    pos = get_stop_record_pos()
    if pos == None:
        print( "--------------------> stop record get buttom: ", pos )
        exit(-1)
    time.sleep(0.1)
    ag.click( pos.left, pos.top )
    time.sleep(1)


def record_video(addr):
    chrome_into_address( addr )
    chrome_100ask_play_frome_zero()
    time.sleep(10)
    wait_play_end()

for i in range( len(G_RECORD_ADDRESS) ):
    print( "--------------------> start record" )
    start_record()
    print( "--------------------> start playing" )
    record_video( G_RECORD_ADDRESS[ i ] )
    print( "--------------------> stop record " )
    stop_record()
    print( "--------------------> stopped " )

