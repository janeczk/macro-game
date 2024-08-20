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
from func import * 
import const
import threading
import keyboard
import tkinter as tk



#"""        
running = True

# Funkcja do monitorowania klawisza 'y'
def monitor_exit_key():
    global running
    while running:
        if keyboard.is_pressed('y'):
            running = False
            print("Zatrzymanie gry...")
            break
        time.sleep(0.1)

# Funkcja, która uruchamia grę
def start_game():
    global running
    running = True
    
    # Uruchomienie wątku monitorującego klawisz 'y'
    exit_thread = threading.Thread(target=monitor_exit_key)
    exit_thread.start()

    # Ustawienie początkowego stanu gry
    game_state = const.GameState()
    game_state.setGameState({"map_name": "Gvar Hamryd",})
    print(game_state.getGameState())

    while running:
        game_state.current_map.setMapName(clear_map_and_go_to_next_map(game_state, "Gvar Hamryd", "Matecznik Szelestu")) 
        find_player_at_passage(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)

        game_state.current_map.setMapName(clear_map_and_go_to_next_map(game_state, "Matecznik Szelestu", "Rozlewisko Kai"))
        find_player_at_passage(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)

        game_state.current_map.setMapName(clear_map_and_go_to_next_map(game_state, "Rozlewisko Kai", "Gvar Hamryd"))
        sell_items_tunia()
        find_player_at_passage(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state)


    exit_thread.join()

# Funkcja zatrzymująca grę
def stop_game():
    global running
    running = False

# Funkcja do tworzenia GUI
def create_gui():
    root = tk.Tk()
    root.title("Gra Automatyczna")

    start_button = tk.Button(root, text="Start", command=start_game)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", command=stop_game)
    stop_button.pack(pady=10)

    exit_button = tk.Button(root, text="Wyjście", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_game()
#"""       
##########################DO DEBUGOWANIA#############################
##threading 
    
"""
time.sleep(5)
while(keyboard.is_pressed('y')== False):
    x,y = FindMobAndGo()
    print(x,y)
    while CheckPlayer(x,y) == False:
        time.sleep(wait()[0])
        print("waiting for player\n")
    time.sleep(3*wait()[0])
    if CheckPlayer(x,y) == True:
        pyautogui.keyDown('e')
        time.sleep(wait()[0])
        pyautogui.keyUp('e')
    else:
        break
    
"""
"""
time.sleep(5)
pyautogui.moveTo(int(204 + 6.2 + 16 * xjump_Gvar_Hamryd), int(198 + 6.2 + 72*yjump_Gvar_Hamryd))
pyautogui.displayMousePosition()
"""
