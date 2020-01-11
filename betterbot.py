# from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
from multiprocessing import Process, Value, Array, Manager
import threading
import ctypes
from PIL import ImageGrab, Image
import pytesseract
import cv2
import numpy as nm
import time
import pyautogui
import random
import imagehash
from random import random


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
    keyMove(['w', 'a'], 3.261)
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

    keyMove(['w', 'a'], 1.629)
    keyMove('w', 4)
    keyMove(['right'], .33)
    time.sleep(1)
    pyautogui.hotkey('shift', 'g')
    time.sleep(6)
    for i in range(0, 6):
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


def drinkWater():
    pyautogui.press('l')


def castWater():
    pyautogui.press(';')


def randomSpell():
    time.sleep(1)
    spells = [castNova, castAE, castShield, jump]
    spells[random.randint(0, 3)]()


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
    releaseSpirit = ImageGrab.grab(bbox=(1300, 380, 1500, 420))
    rs_string = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(releaseSpirit), cv2.COLOR_BGR2GRAY),
        lang='eng')
    print(rs_string)
    if rs_string == 'Release Spirit':
        print(rs_string)
        pyautogui.moveTo(690, 197)
        pyautogui.leftClick()


def targetBM():
    nugget = ImageGrab.grab(bbox=(2330, 340, 2355, 368))
    hash = imagehash.average_hash(nugget)
    template = imagehash.average_hash(Image.open('nugget.jpg'))
    diff = hash - template
    print(diff)
    if diff > 10:
        time.sleep(3)
        pyautogui.press('p')
        pyautogui.press('\\')
        pyautogui.moveTo(310, 260)
        time.sleep(1)
        pyautogui.leftClick()
        pyautogui.moveTo(310, 485)
        time.sleep(1)
        pyautogui.leftClick()
    else:
        return True
    return False


def joinBattle():
    time.sleep(2)
    jb = ImageGrab.grab(bbox=(1200, 380, 1400, 420))
    jb_string = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(jb), cv2.COLOR_BGR2GRAY),
        lang='eng')
    print(jb_string)
    if jb_string == "Enter Battle" or jb_string == "Teta orsteeC Sy" or jb_string == "elt tae et aeles" or jb_string == "Frnter Battle":
        pyautogui.moveTo(630, 205)
        pyautogui.leftClick()
        return True
    return False


def leaveBattle():
    lb = ImageGrab.grab(bbox=(1350, 1080, 1550, 1120))
    lb_str = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(lb), cv2.COLOR_BGR2GRAY),
        lang='eng')
    time.sleep(1)
    if lb_str == "Leave Battleground":
        pyautogui.moveTo(700, 540)
        pyautogui.leftClick()
        return True
    return False


#  ACCEPT
# cap =ImageGrab.grab(bbox=(1200, 380, 1400, 420))
#
# CANCEL
# ImageGrab.grab(bbox=(1300, 380, 1500, 420))
# if cancel & alterac valley, in cave again

# almost the nugger
# cap = ImageGrab.grab(bbox=(2330,340,2355,368))

# cap = ImageGrab.grab(bbox=(2120,130,2170,180))

# REleASE SPIRIT
# cap = ImageGrab.grab(bbox=(1300, 380, 1500, 420))

# ENTER BATTLE
# ImageGrab.grab(bbox=(1200, 380, 1400, 420))

# almost leave BG
# cap = ImageGrab.grab(bbox=(1350, 1080, 1550, 1120))

# is queued ?
# import imagehash
# cap = ImageGrab.grab(bbox=(2320,330,2370,380))
# hash = imagehash.average_hash(cap)
# otherhash = imagehash.average_hash(Image.open('nugget.jpg'))
# if less than 10
# print(hash - otherhash)
if __name__ == "__main__":
    def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    zone = Manager().Value(ctypes.c_char_p, 'zone')
    ZONE = 'Royal Quarter'

    def processZone():
        cap = ImageGrab.grab(bbox=(2300, 100, 2500, 124))
        # cap.show()
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')
        cap = ImageGrab.grab(bbox=(2300, 100, 2500, 124))
        # cap.show()
        tesstr2 = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        cap = ImageGrab.grab(bbox=(2300, 100, 2500, 124))
        # cap.show()
        tesstr3 = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')
        try:
            print([tesstr, tesstr2, tesstr3])
        except:
            print('bad printing')
        if ZONE in [tesstr, tesstr2, tesstr3]:
            zone.value = ZONE
        else:
            zone.value = tesstr3

    # zone_process = Process(target=processZone, args=[zone])
    set_interval(processZone, 10)
    processZone()
    try:
        print(zone.value)
    except:
        print('bad printing')

    running = True
    drink_counter = 0
    if zone.value == ZONE:
        print('not in av to start')
        origin = 'HR'
        queued = False
        joined = False
        left = True
    else:
        print('av to start')
        origin = 'AV'
        queued = True
        joined = True
        left = False
    origin = 'HR'
    move_counter = 0
    while running is True:
        processZone()
        print(f'q: {queued}, j: {joined}, l:{left}')
        if (zone.value == ZONE and queued == False and joined == False) or left == True:
            move_counter = 0
            print('queueing')
            left = False
            queue = targetBM()
            queued = queue
            origin = 'HR'
        elif queued == True and joined == False:
            print(f'waiting to join, drink_counter:{drink_counter}')
            if queued == True:
                pyautogui.press('/')
            join = joinBattle()
            joined = join
            if drink_counter > 5:
                castWater()
            time.sleep(5)
            if drink_counter > 5:
                drinkWater()
                drink_counter = 0
            drink_counter += 1
        else:
            if origin == 'HR':
                joined = False
                queued = False
                time.sleep(15)
                if zone.value != ZONE:
                    queue_counter = 0
                    moveToDoor()
                    time.sleep(90)
                    moveToField()
                    origin = 'AV'
            if "Graveyar" in zone.value or "Winterax Hold" in zone.value:
                move_counter = 0
                ghosted = True
                while ghosted == True:
                    cancel = ImageGrab.grab(bbox=(1300, 380, 1500, 420))
                    cancel_string = pytesseract.image_to_string(
                        cv2.cvtColor(nm.array(cancel), cv2.COLOR_BGR2GRAY),
                        lang='eng')
                    print(cancel_string)
                    if cancel_string == 'Cancel':
                        time.sleep(5)
                    else:
                        ghosted = False
                pyautogui.hotkey('shift', 'g')
                time.sleep(5)
                if zone.value != ZONE:
                    if 'blood' in zone.value or "Snowfall" in zone.value:
                        keyMove('d', 20)
                    else:
                        keyMove('w', 20)
            time.sleep(2)
            leave = leaveBattle()
            castWater()
            if left == False and move_counter < 3:
                keyMove(['right'], random())
                keyMove('w', 10)

                leave = leaveBattle()
                move_counter += 1
            time.sleep(5)
            releaseSpirit()
            drinkWater()
            left = leave
            time.sleep(5)
