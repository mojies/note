import pyautogui as ag
import time

def start_record():
    with ag.hold('win'):
        with ag.hold('shift'):
            time.sleep(0.1)
            ag.keyDown( 's' )
            ag.keyUp( 's' )
            time.sleep(0.1)

    # ag.keyDown('win')
    # ag.keyDown( 'shift' )
    # ag.press( 'r' )
    # ag.keyUp('shift')
    # ag.keyUp('win')
start_record()
