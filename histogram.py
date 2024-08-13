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

arr = []
for i in range(100000):
    arr.append(round(func.wait()[0],4))
plt.hist(arr,bins=200,range=[0,2])
plt.show() 