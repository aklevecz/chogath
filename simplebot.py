import pyautogui
import time
import random

def targetBM():
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite('/tar Taim Ragetotem')
    pyautogui.press('enter')
    pyautogui.press('num7')
    pyautogui.moveTo(9500,660)
    time.sleep(1)
    pyautogui.leftClick()
    pyautogui.moveTo(9500,1300)
    time.sleep(1)
    pyautogui.leftClick()

def moveOutOfCave():
    time.sleep(3)
    pyautogui.keyDown('w')
    counter = 0
    while counter < 5:
        joinBattle()
        time.sleep(2)
        pyautogui.keyDown('a')
        time.sleep(2)
        pyautogui.keyUp('a')
        counter += 1
    time.sleep(10)
    pyautogui.keyUp('w')

def castNova():
    pyautogui.press('3')

def castAE():
    pyautogui.press('e')

def castShield():
    pyautogui.press('r')

def jump():
    pyautogui.press('space')

def joinBattle():
    time.sleep(2)
    pyautogui.moveTo(10700,500)
    pyautogui.leftClick()

def releaseSpirit():
    pyautogui.moveTo(11000,480)
    pyautogui.leftClick()

def leaveBattle():
    time.sleep(2)
    pyautogui.moveTo(11000,1450)
    pyautogui.leftClick()


if __name__ == "__main__":
    def runMove():
        targetBM()
        joinBattle()
        releaseSpirit()
        joinBattle()
        time.sleep(30)
        randomSpell()
        joinBattle()
        moveOutOfCave()
        joinBattle()
        randomSpell()
        time.sleep(10)
        randomSpell()
        joinBattle()
        leaveBattle()
        time.sleep(10)
        randomSpell()
        targetBM()
        runMove()
    
    def randomSpell():
        time.sleep(1)
        spells = [castNova, castAE, castShield, jump]
        spells[random.randint(0,3)]()

    runMove()