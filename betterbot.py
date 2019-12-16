from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
from PIL import ImageGrab, Image
import pytesseract
import cv2
import numpy as nm
import time
import pyautogui
import random

def castNova():
    pyautogui.press('3')

def castAE():
    pyautogui.press('e')

def castShield():
    pyautogui.press('r')

def jump():
    pyautogui.press('space')

def randomSpell():
    time.sleep(1)
    spells = [castNova, castAE, castShield, jump]
    spells[random.randint(0,3)]()

def moveOutOfCave():
    time.sleep(3)
    pyautogui.keyDown('w')
    counter = 0
    while counter < 5:
        leaveBattle()
        releaseSpirit()
        time.sleep(2)
        pyautogui.keyDown('a')
        time.sleep(2)
        pyautogui.keyUp('a')
        counter += 1
    time.sleep(10)
    leaveBattle()
    releaseSpirit()
    pyautogui.keyUp('w')

def releaseSpirit():
    pyautogui.moveTo(2080,650)
    pyautogui.leftClick()

def targetBM():
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite('/tar Taim Ragetotem')
    pyautogui.press('enter')
    pyautogui.press('num7')
    pyautogui.moveTo(180,910)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(580,1810)
    time.sleep(1)
    pyautogui.leftClick()

def joinBattle():
    time.sleep(2)
    pyautogui.moveTo(1980,710)
    pyautogui.leftClick()

def leaveBattle():
    time.sleep(2)
    pyautogui.moveTo(2100,2050)
    pyautogui.leftClick()

wow_window = False
running = True
while wow_window is False:
    if GetWindowText(GetForegroundWindow()) != "World of Warcraft":
        print('NOT WOW')
    else:
        print("YES WOW")
        wow_window = True

        while running is True:
            rect = GetWindowRect(GetForegroundWindow())

            cap = ImageGrab.grab(bbox=(3980,66,4400,115))
#            cap.show()
            tesstr = pytesseract.image_to_string( 
                    cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
                    lang ='eng')
            print(tesstr)
            if tesstr == 'Hunter Rise':
                targetBM()
                joinBattle()
                time.sleep(30)
            else:
                moveOutOfCave()
                leaveBattle()
                randomSpell()
                time.sleep(20)
                releaseSpirit()
                leaveBattle()
