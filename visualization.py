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


def create_hist(n):
    arr = []
    for i in range(n):
        arr.append(func.wait())
    plt.hist(arr,bins=100,range=[0,2])
    plt.show() 

create_hist(10000)
