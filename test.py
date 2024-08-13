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
import func#dupa
import const
import threading
from const import GameState as game_state # dla ulatwienia pisania kodu

starting_state ={
    "map_name": "Gvar Hamryd",
    "player_coords": [63, 42],
    "mob_coords": [0, 0],
}
game_state = const.GameState()
game_state.setGameState(starting_state)
print(game_state.getGameState())

game_state.current_map.setMapName(func.clearMap(game_state,"Gvar Hamryd","Matecznik Szelestu")) #czyszenie Gvar Hamryd
func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)#sprawdzanie wejscia w Mateczniku

game_state.current_map.setMapName(func.clearMap(game_state,"Matecznik Szelestu","Liściaste Rozstaje"))#czyszczenie Matecznika


#odtad zaczynasz kurwo robote
func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)#sprawdzanie wejscia w Lisciastych

game_state.current_map.setMapName(func.clearMap(game_state,"Liściaste Rozstaje","Gvar Hamryd"))#


#game_state.current_map.setMapName("Matecznik Szelestu")#debug
"""
func.FindPlayerAtEntrance(const.przejsciaMS, game_state)
#print(game_state.player_coords.getPlayerXY())#debug
while game_state.current_map.getMapName() == "Matecznik Szelestu":
    if func.goToClosest(const.driadyMS,game_state):
        pag.moveTo(1200 + func.randomPos() * 10, 1000 + func.randomPos() * 10)
        func.FindPlayer(game_state)
        time.sleep(func.wait()[0])
        func.attackMob()
        time.sleep(0.2+func.wait()[0])
    else:
        func.click(game_state.startMiniMap.getStartMiniMap()[0] + (23+0.5) * game_state.mapSize.getStepX() + func.randomPos(),game_state.startMiniMap.getStartMiniMap()[1] + (0+0.5) * game_state.mapSize.getStepY() + func.randomPos())#pozycja przejsca z MS na RK
        pag.moveTo(1200 + func.randomPos() * 10, 1000 + func.randomPos() * 10)
        #aktualizacja informacji o mapie
        game_state.current_map.setMapName("Liściaste Rozstaje")
        game_state.startMiniMap.setStartMiniMap([7,253])
        game_state.endMiniMap.setEndMiniMap([820,796])
        game_state.mapSize.setMapSize([96,64])


func.FindPlayerAtEntrance(const.przejsciaMS, game_state)
while game_state.current_map.getMapName() == "Liściaste Rozstaje":
    if func.goToClosest(const.driadyMS,game_state):
        pag.moveTo(1200 + func.randomPos() * 10, 1000 + func.randomPos() * 10)
        func.FindPlayer(game_state)
        time.sleep(func.wait()[0])
        func.attackMob()
        time.sleep(0.2+func.wait()[0])
    else:
        func.click(game_state.startMiniMap.getStartMiniMap()[0] + (23+0.5) * game_state.mapSize.getStepX() + func.randomPos(),game_state.startMiniMap.getStartMiniMap()[1] + (0+0.5) * game_state.mapSize.getStepY() + func.randomPos())#pozycja przejsca z MS na RK
        pag.moveTo(1200 + func.randomPos() * 10, 1000 + func.randomPos() * 10)
        game_state.setGameState(starting_state)
"""
"""
    if func.FindShortestCords is None:
        func.click(const.startGH.x + (0+0.5) * const.xStepGH + func.randomPos(),const.startGH.y + (79+0.5) * const.yStepGH + func.randomPos())#pozycja przejsca z GH na MS
        if const.currentMap.name == "Matecznik szelestu":
            func.FindPlayerAtEntrance(const.przejsciaMS)
x=16
y=14
print(pag.pixel(int(const.startGH.x + (x + 0.5)* const.xStepGH),int(const.startGH.y + (y + 0.5)*const.yStepGH)))
pag.moveTo(const.startGH.x + (x + 0.5)* const.xStepGH,const.startGH.y + (y + 0.5)*const.yStepGH)
#print(pag.pixel(int(const.startGH.x + (53 + 0.5)* const.xStepGH),int(const.startGH.y + (43 + 0.5)*const.yStepGH)))
#win32api.SetCursorPos((int(const.startGH.x + (const.przejsciaGH[0][0] + 0.5)* const.xStepGH),int(const.startGH.y + (const.przejsciaGH[0][1] + 0.5)*const.yStepGH)))
"""
#pag.moveTo((const.startGH.x + (const.przejsciaGH[0][0] + 0.5)* const.xStepGH),(const.startGH.y + (const.przejsciaGH[0][1] + 0.5)*const.yStepGH))
#pag.displayMousePosition()