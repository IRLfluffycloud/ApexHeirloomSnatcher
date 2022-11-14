import pyautogui as p
import keyboard
from dataclasses import dataclass

p.FAILSAFE = False

@dataclass
class Character:
    OCTANE     = (423, 569)
    WRAITH     = (705, 437)
    GIBRALTAR  = (348, 437)
    LOBA       = (143, 703)
    CRYPTO     = (665, 573)
    WATTSON    = (533, 565)
    VALKYRIE   = (624, 688)
    PATHFINDER = (580, 440)
    
def POP_BACK_TO_LOBBY():
    """RUN WHILE IN APEX LOBBY"""
    screenWidth, screenHeight = p.size()
    screenCenter = (screenWidth / 2, screenHeight / 2)
    p.click(screenCenter)
    p.press('esc')
    p.typewrite('r')
    p.moveTo(1393, 1011)
    p.click()
    p.moveTo(844, 716)
    p.click()
    p.click()

def GET_HEIRLOOM(characterCoords):
    p.moveTo(945, 47) # LEGENDS menu button
    p.click()
    p.moveTo(characterCoords)
    p.click()
    p.moveTo(1557, 802) # HEIRLOOM
    p.click()

def FROM_HEIRLOOM_TO_LOBBY():
    p.press('esc')
    p.press('esc')
    POP_BACK_TO_LOBBY()


CHARACTER_OF_CHOICE = Character.PATHFINDER
while True:
    print(p.position())
    if keyboard.is_pressed('a'):
        POP_BACK_TO_LOBBY()
    if keyboard.is_pressed('s'):
        GET_HEIRLOOM(CHARACTER_OF_CHOICE)
    if keyboard.is_pressed('w'):
        FROM_HEIRLOOM_TO_LOBBY()
    if keyboard.is_pressed('d'):
        GET_HEIRLOOM(CHARACTER_OF_CHOICE)
        FROM_HEIRLOOM_TO_LOBBY()