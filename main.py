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




#"""        

running = True

def monitor_exit_key():
    global running
    while running:
        if keyboard.is_pressed('F7'):
            running = False
            print("Program zatrzymany")
            break
        time.sleep(0.01)  # Zmniejszenie obciążenia CPU

def main():
    global running
    # Uruchomienie wątku monitorującego klawisz 'y'
    exit_thread = threading.Thread(target=monitor_exit_key)
    exit_thread.start()
    time.sleep(5)

    while running:
        x, y = func.GetMob()
        if x == -1:
            a = random.randint(205, 980)
            b = random.randint(200, 1350)
            pag.click(a, b)
            time.sleep(func.wait()[0] * 3)
        else:
            time.sleep(func.wait()[0])
            pag.click(x + random.randint(-40, 40) / 10, y + random.randint(-40, 40) / 10)
            pyautogui.moveTo(1300 + func.randomPos() * 1000, 700 + func.randomPos() * 1000)
            func.CheckPlayer(x, y)
            time.sleep(func.wait()[0] / 5)
            pyautogui.keyDown('e')
            time.sleep(func.wait()[0] / 10)
            pyautogui.keyUp('e')
            time.sleep(func.wait()[0] / 2)
    
    # Zatrzymanie wątku monitorującego po zakończeniu głównej pętli
    exit_thread.join()

if __name__ == "__main__":
    main()
#"""       


    
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
