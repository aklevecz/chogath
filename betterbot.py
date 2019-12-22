# from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
from PIL import ImageGrab, Image
import pytesseract
import cv2
import numpy as nm
import time
import pyautogui
import random

def keyMove(k, t):
    for key in k:
        pyautogui.keyDown(key)
    time.sleep(t)
    for key in k:
        pyautogui.keyUp(key)

def moveToDoor():
    print('door move')
    # keyMove('w', 2.188)
    # keyMove('a', 1.789)
    # keyMove('w', 4.733)
    # keyMove('a', 1)
    # keyMove('w', 3.5)
    # --------------------
    keyMove(['w','a'], 3.261)
    keyMove('w', 7.442)



def moveToField():
    # keyMove('w', 5.472)
    # keyMove('d', 9)
    # keyMove('w', 2.2)
    # keyMove('d', 2.8)
    # keyMove('w', 1)
    # keyMove('d', 2.7)
    # keyMove('w', .8 )
    # keyMove('d', 15)
    # keyMove('w', 1.5)

    keyMove(['w','a'], 1.629)
    keyMove('w', 4)
    keyMove(['right'], .33)
    pyautogui.hotkey('shift', 'g')
    time.sleep(5)
    for i in range(0,6):
        keyMove('w', 10)
        jump()

def castNova():
    pyautogui.press('3')

def castAE():
    pyautogui.press('e')

def castShield():
    pyautogui.press('r')

def jump():
    pyautogui.press('space')

def castInt():
    pyautogui.press('l')

def castRuby():
    pyautogui.press(';')

def randomSpell():
    time.sleep(1)
    spells = [castNova, castAE, castShield, jump]
    spells[random.randint(0,3)]()
def moveOutOfCave():
    castShield()
    time.sleep(3)
    pyautogui.keyDown('w')
    counter = 0
    while counter < 5:
        releaseSpirit()
        jump()
        time.sleep(3)
        pyautogui.keyDown('a')
        pyautogui.keyUp('w')
        jump()
        time.sleep(5)
        pyautogui.keyDown('w')
        pyautogui.keyUp('a')
        jump()
        counter += 1
    time.sleep(10)
    jump()
    castShield()
    releaseSpirit()
    pyautogui.keyUp('w')
def releaseSpirit():
    pyautogui.moveTo(690,197)   
    pyautogui.leftClick()

def targetBM():
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite('/tar Grizzle Halfmane')
    pyautogui.press('enter')
    pyautogui.press('\\')
    pyautogui.moveTo(310,258)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(310,485)
    time.sleep(1)
    pyautogui.leftClick()

def joinBattle():
    time.sleep(2)
    pyautogui.moveTo(630,205)
    pyautogui.leftClick()

def leaveBattle():
    time.sleep(2)   
    pyautogui.moveTo(700,540)
    pyautogui.leftClick()

from multiprocessing import Process, Value, Array, Manager
import ctypes
import threading

    

if __name__ == "__main__":
    def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    zone = Manager().Value(ctypes.c_char_p, 'zone')

    def processZone():
        cap = ImageGrab.grab(bbox=(2300,100,2500,124))
        # cap.show()
        tesstr = pytesseract.image_to_string( 
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
                lang ='eng')
        cap2 = ImageGrab.grab(bbox=(2300,100,2500,124))
        # cap.show()
        tesstr2 = pytesseract.image_to_string( 
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
                lang ='eng')
        
        cap = ImageGrab.grab(bbox=(2300,100,2500,124))
        # cap.show()
        tesstr3 = pytesseract.image_to_string( 
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
                lang ='eng')
        try:
            print([tesstr, tesstr2, tesstr3])
        except:
            print('bad printing')
        if 'Royal Quarter' in [tesstr, tesstr2, tesstr3]:
            zone.value = 'Royal Quarter'
        else:
            zone.value = tesstr3

    # zone_process = Process(target=processZone, args=[zone])
    set_interval(processZone, 10)
    processZone()
    try:
        print(zone.value)
    except:
        print('bad printing')
    wow_window = False
    running = True
    if zone.value == 'Royal Quarter':
        origin = 'HR'
    else:
        origin = 'AV'
    #origin = 'HR'
    while running is True:
        processZone()
        if zone.value == 'Royal Quarter':
            targetBM()
            castRuby()
            joinBattle()
            time.sleep(30)
            castInt()
            origin = 'HR'
        else:
            if origin == 'HR':
                time.sleep(15)
                if zone.value != 'Royal Quarter':
                    moveToDoor()
                    time.sleep(60)
                    moveToField()
                    time.sleep(90)
                    origin = 'AV'
            if "Graveyard" in zone.value:
                time.sleep(30)
                pyautogui.hotkey('shift', 'g')
                time.sleep(5)
                keyMove('d', 20)
            leaveBattle()
            randomSpell()
            time.sleep(31)
            if "Graveyard" not in zone.value:
                releaseSpirit()
            leaveBattle()
            time.sleep(5)
