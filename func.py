from pyautogui import * # type: ignore
import pyautogui # type: ignore
import pyautogui as pag # type: ignore
import time
import keyboard # type: ignore
import numpy as np # type: ignore
import random
import win32api, win32con # type: ignore
import matplotlib.pyplot as plt # type: ignore
from const import *
from const import GameState as game_state # dla ulatwienia pisania kodu


def sell_items_tunia():# funkcja typowo brute-force, za duzo liczenia i opracowywania roznych map
    click(180 + random_pos(), 400 + random_pos())  # przejście do domu Tuni
    find_player_by_pixels(492, 755)
    click(1275 + random_pos(), 808 + random_pos())  # klik na Tunię
    find_player_by_pixels(438, 602)
    
    pag.keyDown('1')  # wejście w dialog
    time.sleep(wait()[0] / 15)
    pag.keyUp('1')
    time.sleep(wait()[0] / 5)
    
    clear_bag(1420, 789)  # sprzedanie torby 1
    clear_bag(1461, 798)  # sprzedanie torby 2
    clear_bag(1419, 842)  # sprzedanie torby 3
    time.sleep(wait()[0] / 5)
    pag.keyDown('esc')  # zamknięcie dialogu
    time.sleep(wait()[0] / 15)
    pag.keyUp('esc')
    
    click(492 + random_pos(), 755 + random_pos())  # klik na exit
    time.sleep(wait()[0])

    find_player_by_pixels(172, 401)  # sprawdzanie czy przeszedł
    click(418 + random_pos(), 257 + random_pos())  # klik na exit
    time.sleep(wait()[0])

    find_player_by_pixels(426, 791)
    click(290 + random_pos(), 257 + random_pos())  # klik na exit
    time.sleep(wait()[0])

    find_player_by_pixels(299, 791)
    click(11 + random_pos(), 614 + random_pos())  # klik na exit


def clear_bag(x,y):
    for i in range(2):
        click(x+random_pos(),y+random_pos())
        time.sleep(wait()[0])
        click(1459+random_pos(),986+random_pos())
        time.sleep(wait()[0])

def find_player_by_pixels(x,y):
    while True:
        if  pag.pixelMatchesColor(int(x),int(y),player_color,tolerance=15) or \
            pag.pixelMatchesColor(int(x+8.5),int(y),player_color,tolerance=15) or\
            pag.pixelMatchesColor(int(x-8.5),int(y),player_color,tolerance=15):
            break
    print("player found!")
    time.sleep(0.3+wait()[0])

def tp_kwiaty():
    pag.keyDown('4')
    time.sleep(wait()[0]/10)
    pag.keyUp('4')

def click(x,y):
    pag.moveTo((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(wait()[0]/15)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def attack_mob():
    pag.keyDown('e')
    time.sleep(wait()[0]/15)
    pag.keyUp('e')



def wait():
    x = np.random.normal(0.5,0.3,1)
    if x < 0 :  return -x + random.randrange(0,200)/1000
    if x < 0.1 :return x + random.randrange(50,200)/1000 
    if x > 1.5 : return x - random.randrange(0,500)/1000 
    return x

def random_pos():
    if random.randint(0,1) == 0:
        return random.randint(10,50)/100
    return -random.randint(10,50)/100

def transfer_coords_to_pixels_XY(coords,game_state):#coords = [x,y]
    return game_state.start_mini_map.getStartMiniMap()[0] + (coords[0]+0.5) * game_state.map_size.getStepX(), game_state.start_mini_map.getStartMiniMap()[1] + (coords[1]+0.5) * game_state.map_size.getStepY()

def find_player_at_passage(passage,game_state):
    print("Waiting for player to show at the entrance in:", game_state.current_map.getMapName())
    while True:
        for XY_coords in passage:
            x, y = transfer_coords_to_pixels_XY(XY_coords,game_state)
            if pag.pixelMatchesColor(int(x),int(y),player_color,tolerance=15):
                game_state.player_coords.setPlayerXY(XY_coords[0],XY_coords[1])
                print(f"Player found at entrance at: {game_state.player_coords.getPlayerXY()} at map {game_state.current_map.getMapName()}")
                return
        time.sleep(0.5+wait()[0])


def path_length(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def check_mob(x,y,game_state):
    tab = [x,y]
    xCord,yCord = transfer_coords_to_pixels_XY(tab,game_state)
    if pag.pixelMatchesColor(int(xCord),int(yCord),mob_color,tolerance=50):
        return True
    return False

def print_route(game_state):
    print(f"Travelling from {game_state.player_coords.getPlayerXY()} to {game_state.mob_coords.getMobXY()} at map {game_state.current_map.getMapName()}")


def find_shortest_coords(mob_coords,game_state):
    shortestPath = 999
    for XY_coords in mob_coords:
        if not check_mob(XY_coords[0],XY_coords[1],game_state):
            continue

        #obsluga wyjatkow
        if game_state.mob_coords.getMobXY() == [46,19] and XY_coords[0] == 25 and XY_coords[1] == 15 and game_state.current_map.getMapName() == "Gvar Hamryd": #wyjatek dla trasy 
            print("Skipping path from [46,19] to [25,15] at Gvar Hamryd")#[25,15]dest#[46,19]#ignore the route
            continue
        if game_state.mob_coords.getMobXY() == [24,83]  and game_state.current_map.getMapName() == "Matecznik Szelestu":#wyjatek dla trasy, z danego moba przechodzi na kolejnego, usprawnienie routa
            shortestPathCords = [11,84]
            shortestPath = 998
            break
        ######
        #print(f"Checking path from {game_state.player_coords.getPlayerXY()} to {XY_coords} at map {game_state.current_map.getMapName()}")
        currentPath = path_length(game_state.player_coords.getPlayerX(),game_state.player_coords.getPlayerY(),XY_coords[0],XY_coords[1])
        if  currentPath < shortestPath:
            shortestPath = currentPath
            shortestPathCords = XY_coords
    if shortestPath == 999:
        print("No path found, proceeding to another map")
        return False
    return shortestPathCords

def go_to_closest(mob_coords,game_state):
    shortest_path_coords = find_shortest_coords(mob_coords,game_state)
    if not shortest_path_coords:
       return 0
    game_state.mob_coords.setMobXY(shortest_path_coords[0],shortest_path_coords[1])
    x,y = transfer_coords_to_pixels_XY(game_state.mob_coords.getMobXY(),game_state)
    print_route(game_state)
    pag.click(x+random_pos(),y+random_pos())
    return 1

def clear_map_and_go_to_next_map(game_state,current_map,next_map):
    print(game_state.getGameState())
    map_properties = map_data.get(current_map)
    while game_state.current_map.getMapName() == current_map:
        if go_to_closest(map_properties.getMobLocations(),game_state):
            pag.moveTo(1200 + random_pos() * 500, 1000 + random_pos() * 500)
            find_player_near_mob(game_state)
            time.sleep(wait()[0]/2)
            attack_mob()
            time.sleep(0.4+wait()[0]/5)
        else:
            if current_map == "Rozlewisko Kai": #wyjatek dla trasy, teleportujacy na kwiaty i sprzedjacy itemy
                time.sleep(wait()[0])
                tp_kwiaty()
                game_state.setGameState({"map_name": next_map}) #aktualizacja info
                current_map = next_map
                return next_map
            x,y = transfer_coords_to_pixels_XY(map_properties.getNextMapCoords(),game_state)
            click(x+random_pos(),y+random_pos())
            pag.moveTo(1200 + random_pos() * 500, 1000 + random_pos() * 500)
            game_state.setGameState({"map_name": next_map})
            current_map = next_map
            return next_map



def find_player_near_mob(game_state):
    print("Waiting for player")
    while True:
        x,y = transfer_coords_to_pixels_XY(game_state.mob_coords.getMobXY(),game_state)
        if pag.pixelMatchesColor(int(x-game_state.map_size.getStepX()),int(y),player_color,tolerance=15):#sprawdzanie pozycji gracza w pozycji krzyza dookola moba
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX()-1,game_state.mob_coords.getMobY())
            return
        elif pag.pixelMatchesColor(int(x),int(y-game_state.map_size.getStepY()),player_color,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX(),game_state.mob_coords.getMobY()-1)
            return
        elif pag.pixelMatchesColor(int(x+game_state.map_size.getStepX()),int(y),player_color,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX()+1,game_state.mob_coords.getMobY())
            return
        elif pag.pixelMatchesColor(int(x),int(y+game_state.map_size.getStepY()),player_color,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX(),game_state.mob_coords.getMobY()+1)
            return
        elif pag.pixelMatchesColor(int(x),int(y),player_color,tolerance=15):
            game_state.player_coords.setPlayerXY(game_state.mob_coords.getMobX(),game_state.mob_coords.getMobY())
            return
        

