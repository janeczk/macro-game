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

game_state = const.GameState()
game_state.setGameState({"map_name": "Rozlewisko Kai",})
func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)#sprawdzanie wejscia w Lisciastych

game_state.current_map.setMapName(func.clearMap(game_state,"Rozlewisko Kai","Gvar Hamryd"))#