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
starting_state ={
    "map_name": "Gvar Hamryd",
    "player_coords": [63, 42],
    "mob_coords": [0, 0],
    "start_mini_map": [142,118],
    "end_mini_map": [685,931],
    "map_size": [64,96],
}
game_state = const.GameState()
game_state.setGameState(starting_state)

game_state.startMiniMap.setStartMiniMap(7,253)#aktualizacja wielkosci mapy
game_state.endMiniMap.setEndMiniMap(820,796)
game_state.mapSize.setMapSize(96,64)