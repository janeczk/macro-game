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
import keyboard



#"""        
running = True

def monitor_exit_key():
    global running
    while running:
        if keyboard.is_pressed('y'):
            running = False
            print("Zatrzymanie gry...")
            break
        time.sleep(0.1)

def main():
    global running
    
    # Uruchomienie wątku monitorującego klawisz 'y'
    exit_thread = threading.Thread(target=monitor_exit_key)
    exit_thread.start()

    # Ustawienie początkowego stanu gry
    game_state = const.GameState()
    game_state.setGameState({"map_name": "Gvar Hamryd",})
    print(game_state.getGameState())

    while running:
        # Sekwencja działań dla kolejnych map
        game_state.current_map.setMapName(func.clearMap(game_state, "Gvar Hamryd", "Matecznik Szelestu")) # Czyszczenie Gvar Hamryd
        func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state) # Sprawdzanie wejścia w Mateczniku

        game_state.current_map.setMapName(func.clearMap(game_state, "Matecznik Szelestu", "Rozlewisko Kai")) # Czyszczenie Matecznika
        func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state) # Sprawdzanie wejścia w Liściastych

        game_state.current_map.setMapName(func.clearMap(game_state, "Rozlewisko Kai", "Gvar Hamryd")) # Czyszczenie Rozlewiska Kai
        func.sellItemsuTuni() # Sprzedaż przedmiotów u Tuni
        func.FindPlayerAtEntrance(const.map_data.get(game_state.current_map.getMapName()).getTransitions(), game_state) # Sprawdzanie wejścia w Gvar Hamryd

        if not running:  # W razie zatrzymania gry przez naciśnięcie 'y'
            break

    # Zatrzymanie wątku monitorującego po zakończeniu głównej pętli
    exit_thread.join()

if __name__ == "__main__":
    main()
#"""       
##########################DO DEBUGOWANIA#############################
##threading 
##przejscia w funkcji u tuni
##rozpoczynanie routow
##srodek mobka sprawdzac
    
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
