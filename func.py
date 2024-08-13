from pyautogui import * # type: ignore
import pyautogui # type: ignore
import pyautogui as pag # type: ignore
import time
import keyboard # type: ignore
import numpy as np # type: ignore
import random
import win32api, win32con # type: ignore
import matplotlib.pyplot as plt # type: ignore
import const
from const import *
from const import GameState as game_state # dla ulatwienia pisania kodu



def click(x,y):
    pag.moveTo((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(wait()[0]/5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def attackMob():
    pag.keyDown('e')
    time.sleep(wait()[0]/10)
    pag.keyUp('e')

def wait():
    x = np.random.normal(0.5,0.3,1)
    if x < 0 :  return -x + random.randrange(0,200)/1000
    if x < 0.1 :return x + random.randrange(50,200)/1000 
    if x > 1.5 : return x - random.randrange(0,500)/1000 
    return x

def randomPos():
    if random.randint(0,1) == 0:
        return random.randint(10,50)/100
    return -random.randint(10,50)/100

def FindPlayerAtEntrance(passage,game_state):
    while True:
        for i in passage:
            x, y = game_state.startMiniMap.getStartMiniMap()[0] + (i[0]+0.5) * game_state.mapSize.getStepX() , game_state.startMiniMap.getStartMiniMap()[1] + (i[1]+0.5) * game_state.mapSize.getStepY()
            if pag.pixelMatchesColor(int(x),int(y),const.playerColor,tolerance=15):
                game_state.player_coords.setPlayerXY(i[0],i[1])
                print(f"Player found at entrance at: {game_state.player_coords.getPlayerXY()} at map {game_state.current_map.getMapName()}")
                return
        print("Waiting for player to show at the entrance in:", game_state.current_map.getMapName())
        time.sleep(0.2)


def pathLength(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def checkMob(x,y,game_state):
    xCord, yCord = game_state.startMiniMap.getStartMiniMap()[0] + (x+0.5) * game_state.mapSize.getStepX(), game_state.startMiniMap.getStartMiniMap()[1] + (y+0.5) * game_state.mapSize.getStepY()
    if pag.pixelMatchesColor(int(xCord),int(yCord),const.mobColor,tolerance=50):
        return True
    return False

def printRoute(game_state):
    print(f"Travelling from {game_state.player_coords.getPlayerXY()} to {game_state.mob_coords.getMobXY()} at map {game_state.current_map.getMapName()}")


def FindShortestCords(passage,game_state):
    shortestPath = 999
    for i in passage:
        if not checkMob(i[0],i[1],game_state):
            continue
        if game_state.mob_coords.getMobXY() == [46,19] and i[0] == 25 and i[1] == 15 and game_state.current_map.getMapName() == "Gvar Hamryd": #wyjatek dla trasy 
            print("Skipping path from [46,19] to [25,15] at Gvar Hamryd")#[25,15]dest#[46,19]start#ignore the route
            continue
        if game_state.mob_coords.getMobXY() == [24,83]  and game_state.current_map.getMapName() == "Matecznik Szelestu":#wyjatek dla trasy, z danego moba przechodzi na kolejnego, usprawnienie routa
            shortestPathCords = [11,84]
            shortestPath = 998
            break
        currentPath = pathLength(game_state.player_coords.getPlayerX(),game_state.player_coords.getPlayerY(),i[0],i[1])
        if  currentPath < shortestPath:
            shortestPath = currentPath
            shortestPathCords = i
    if shortestPath == 999:
        print("No path found, proceeding to another map")
        return False
    return shortestPathCords


def clearMap(game_state,currentMap,nextMap):
    map_properties = const.map_data.get(currentMap)
    while game_state.current_map.getMapName() == currentMap:
        if goToClosest(map_properties.getMobLocations(),game_state):
            pag.moveTo(1200 + randomPos() * 10, 1000 + randomPos() * 10)
            FindPlayer(game_state)
            time.sleep(wait()[0])
            attackMob()
            time.sleep(0.2+wait()[0])
        else:
            click(map_properties.getStartMiniMap()[0] + (map_properties.getNextMapCoords()[0]+0.5) * game_state.mapSize.getStepX() + randomPos(),
                  map_properties.getStartMiniMap()[1] + (map_properties.getNextMapCoords()[1]+0.5) * game_state.mapSize.getStepY() + randomPos()
                  )
            pag.moveTo(1200 + randomPos() * 10, 1000 + randomPos() * 10)
            currentMap = nextMap
            return nextMap

def goToClosest(passage,game_state):
    shortestPathCords = FindShortestCords(passage,game_state)
    if shortestPathCords == False:
       return 0
    game_state.mob_coords.setMobXY(shortestPathCords[0],shortestPathCords[1])
    x,y = game_state.startMiniMap.getStartMiniMap()[0] + (game_state.mob_coords.getMobX()+0.5) * game_state.mapSize.getStepX() + randomPos() , game_state.startMiniMap.getStartMiniMap()[1] + (game_state.mob_coords.getMobY()+0.5) * game_state.mapSize.getStepY() + randomPos()
    printRoute(game_state)
    pag.click(x,y)
    return 1

def FindPlayer(game_state):
    print("Waiting for player")
    while True:
        x,y = game_state.startMiniMap.getStartMiniMap()[0] + (game_state.mob_coords.getMobX()+0.5) * game_state.mapSize.getStepX() , game_state.startMiniMap.getStartMiniMap()[1] + (game_state.mob_coords.getMobY()+0.5) * game_state.mapSize.getStepY()
        if pag.pixelMatchesColor(int(x-game_state.mapSize.getStepX()),int(y),const.playerColor,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX()-1,game_state.mob_coords.getMobY())
            return
        elif pag.pixelMatchesColor(int(x),int(y-game_state.mapSize.getStepY()),const.playerColor,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX(),game_state.mob_coords.getMobY()-1)
            return
        elif pag.pixelMatchesColor(int(x+game_state.mapSize.getStepX()),int(y),const.playerColor,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX()+1,game_state.mob_coords.getMobY())
            return
        elif pag.pixelMatchesColor(int(x),int(y+game_state.mapSize.getStepY()),const.playerColor,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX(),game_state.mob_coords.getMobY()+1)
            return
        time.sleep(0.1)
        
"""
def updatePlayerCords(x,y):
    const.playerCords.x = x
    const.playerCords.y = y
""" 

"""
def FindMobAndGo():
    for i in range(const.Gvar_Hamryd_y):
        for j in range (const.Gvar_Hamryd_x):
            pyautogui.moveTo(int(204 + 6.2 + j * const.xjump_Gvar_Hamryd), int(219 + 6.2 + i*const.yjump_Gvar_Hamryd))
            if pyautogui.pixel( int(204 + 6.2 + j * const.xjump_Gvar_Hamryd), int(219 + 6.2 + i*const.yjump_Gvar_Hamryd) ) [0] <= 246 and pyautogui.pixel( int(204 + 6.2 + j * const.xjump_Gvar_Hamryd), int(219 + 6.2 + i*const.yjump_Gvar_Hamryd) ) [0] >= 239:
                pag.click(int(204 + randomPos() + j* const.xjump_Gvar_Hamryd), int(219 + randomPos() + i*const.yjump_Gvar_Hamryd))
                time.sleep(wait()[0])
                pyautogui.moveTo(600+randomPos()*100,1400+randomPos()*100)
                return int(204 + 6.2 + j * const.xjump_Gvar_Hamryd), int(219 + 6.2 + i*const.yjump_Gvar_Hamryd)
            




def CheckPlayer(x,y):
    while(1):
        print("waiting for player\n")
        if (pyautogui.pixel( int(x+const.xjump_Gvar_Hamryd), int(y) ) [2] == 255) or (pyautogui.pixel( int(x), int(y+const.yjump_Gvar_Hamryd) ) [2] == 255) or (pyautogui.pixel( int(x-const.xjump_Gvar_Hamryd), int(y) ) [2] == 255) or (pyautogui.pixel( int(x), int(y-const.yjump_Gvar_Hamryd) ) [2] == 255):
            return

def GetMob():
    arr = const.driady_GH
    for i in arr:
        a = random.choice(arr)
        if pyautogui.pixel( int(204 + 6.2 + a[0]*const.xjump_Gvar_Hamryd), int(219 + 6.2 + a[1] * const.yjump_Gvar_Hamryd)) [0] <= 246 and pyautogui.pixel( int(204 + 6.2 + a[0]*const.xjump_Gvar_Hamryd), int(219 + 6.2 + a[1] * const.yjump_Gvar_Hamryd)) [0] >= 239:
            arr.remove(a)
            return int(204 + 6.2 + a[0]*const.xjump_Gvar_Hamryd), int(219 + 6.2 + a[1] * const.yjump_Gvar_Hamryd)
    return -1,-1
"""