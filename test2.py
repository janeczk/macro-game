from pyautogui import * # type: ignore
import pyautogui # type: ignore
import pyautogui as pag # type: ignore
import time
import keyboard # type: ignore
import numpy as np # type: ignore
import random
import sys
import win32api, win32con # type: ignore
import matplotlib.pyplot as plt # type: ignore
import func
import const
import threading

#print(const.driadyGH[53])
#print(pag.pixel(int(const.startGH.x + (const.driadyGH[53][0]+0.5)* const.xStepGH),int(const.startGH.y + (const.driadyGH[53][1]+0.5)*const.yStepGH)))
#pag.moveTo(int(const.startGH.x + (const.driadyGH[53][0]+0.5)* const.xStepGH),int(const.startGH.y + (const.driadyGH[53][1]+0.5)*const.yStepGH))
"""
for i in const.driadyMS:
    x = i[0]
    y = i[1]
    print(pag.pixel(int(const.startGH.x + (x + 0.5)* const.xStepGH),int(const.startGH.y + (y + 0.5)*const.yStepGH)),x,y)
    pag.moveTo(int(const.startGH.x + (x + 0.5)* const.xStepGH),int(const.startGH.y + (y + 0.5)*const.yStepGH))
"""
"""
game_state = const.GameState()
game_state.setGameState({"map_name": "Rozlewisko Kai",})
func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)#sprawdzanie wejscia w Lisciastych

game_state.current_map.setMapName(func.clearMap(game_state,"Rozlewisko Kai","Gvar Hamryd"))#
"""
"""
func.click(180+func.randomPos(),400+func.randomPos())#przejscie do domu tuni
time.sleep(0.3+func.wait()[0]/5)
func.click(1275+func.randomPos(),808+func.randomPos())#klik na tunie
time.sleep(func.wait()[0])
pag.keyDown('1')#wejscie w dialog
time.sleep(wait()[0]/15)
pag.keyUp('1')
time.sleep(wait()[0]/5)
func.clearBag(1420,789)#sprzedanie torby 1
func.clearBag(1461,798)#sprzedanie torby 2
func.clearBag(1419,842)#sprzedanie torby 3
pag.keyDown('esc')#zamkniecie dialogu
time.sleep(wait()[0]/15)
pag.keyUp('esc')


"""
"""
func.click(180+func.randomPos(),400+func.randomPos())#przejscie do domu tuni
func.findPlayer(492,755)
func.click(1275+func.randomPos(),808+func.randomPos())#klik na tunie
func.findPlayer(438,602)
pag.keyDown('1')#wejscie w dialog
time.sleep(func.wait()[0]/15)
pag.keyUp('1')
time.sleep(func.wait()[0]/5)
func.clearBag(1420,789)#sprzedanie torby 1
func.clearBag(1461,798)#sprzedanie torby 2
func.clearBag(1419,842)#sprzedanie torby 3
pag.keyDown('esc')#zamkniecie dialogu
time.sleep(func.wait()[0]/15)
pag.keyUp('esc')
func.click(492+func.randomPos(),755+func.randomPos())#klik na exit
time.sleep(func.wait()[0])

func.findPlayer(172,401)#sprawdzanie czy przeszedl
func.click(418+func.randomPos(),257+func.randomPos())#klik na exit
time.sleep(func.wait()[0])

func.findPlayer(418,791)
func.click(290+func.randomPos(),257+func.randomPos())#klik na exit
time.sleep(func.wait()[0])

func.findPlayer(299,791)
func.click(11+func.randomPos(),614+func.randomPos())#klik na exit


game_state = const.GameState()
game_state.setGameState({"map_name": "Gvar Hamryd",})
print(game_state.getGameState())

func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)
"""