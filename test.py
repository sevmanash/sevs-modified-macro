
import pyautogui as pag
import time
import os
import tkinter
import move
import sys
import cv2
from PIL import ImageGrab, Image
import numpy as np
import imagesearch
import loadsettings
import subprocess
import tkinter as tk
import tty
from tkinter import ttk
import backpack
from webhook import webhook
import webbrowser
import reset
import _darwinmouse as mouse
import ast
import getHaste
from datetime import datetime
import matplotlib.pyplot as plt
import random
from matplotlib.colors import from_levels_and_colors
from matplotlib.collections import LineCollection
import math
from pynput.keyboard import Key, Controller
import pynput
from pynput.mouse import Button
import Quartz.CoreGraphics as CG
import struct
import reset
from pixelcolour import getPixelColor
import pygetwindow as gw
from logpy import log
keyboard = Controller()
mouse = pynput.mouse.Controller()

def roblox():
    cmd = """
    osascript -e 'activate application "Roblox"' 
    """
    os.system(cmd)
    time.sleep(1)

def terminal():
    cmd = """
    osascript -e 'activate application "Terminal"' 
    """
    os.system(cmd)
    time.sleep(1)
def loadRes():
    outdict =  {}
    with open('save.txt') as f:
        lines = f.read().split("\n")
    f.close()
    for s in lines:
        l = s.replace(" ","").split(":")
        if l[1].isdigit():
            l[1] = int(l[1])
        outdict[l[0]] = l[1]
    return outdict

fields = {}

while True:
    field = input("field: ")
    if field == "quit": break
    gp = input("gather pattern: ")
    gs = "s"
    gw = 2
    gt = 8
    pack = 100
    bgt = input("before gather turn: ")
    tt = input("turn times")
    rth = "walk"
    ws = 1
    sl = input("start location: ")
    dfc = input("distance from center: ")
    fdc = 0
    fields[field] = {
        "gather_pattern": gp,
        "gather_width": gw,
        "gather_time": gt,
        "pack": pack,
        "before_gather_turn": bgt,
        "turn_times": tt,
        "return_to_hive": rth,
        "whirligig_slot": ws,
        "start_location": sl,
        "distance_from_center": dfc,
        "field_drift_compensation": fdc
        

        }
print(fields)
                    
'''
screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
small_image = cv2.imread('./images/general/nightsky.png')
large_image = screen
res = cv2.matchTemplate(small_image, large_image, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
x,y = max_loc
print("Trying to find night sky. max_val is {} ".format(max_val))
MPx,MPy = min_loc

print(MPx,MPy)
pag.moveTo(MPx//2,MPy//2)
# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]
# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)
# The image is only displayed if we call this
cv2.waitKey(0)

if max_val >= 0.5:
    return [1,x,y,max_val]
return
'''

'''

times = []
start = time.time()
for _ in range(5):
    start = time.time()
    move.press(",")
    move.press("e")
    time.sleep(0.8)
    pag.keyDown("w")
    move.press("space")
    move.press("space")
    time.sleep(9)
    pag.keyUp("w")
    move.press("space")
    times.append(time.time()-start)
print(sum(times)/len(times))
'''

'''
# For both Python 2.7 and Python 3.x
from PIL import Image
img_data = b'iVBORw0KGgoAAAANSUhEUgAAAJ8AAAAWAQMAAADkatyzAAAABlBMVEUAAAAbKjWMzP1VAAAAAXRSTlMAQObYZgAAAdlJREFUeAEBzgEx/gD4AAAAAAAAAAAAAAAAAAAAAAAAAAD+BgAAAAAADAAAAAHgDAAAAEAAAAD/BgAAAAB+DAAAAAH+DAAAAEAAAACBhgAAAACCDAAAAAECDAAAAEAAAACBhgAAAAGADAAAAAEDDAAAAEAAAACBhjBAAAGADB8MDAEDDB8MAfAAJgCBBjBB8AEADAGEDAEDDAGP4fD4PAD/BjBCCAEADACECAH+DACMEEEEMAD+BjBCCAEADACGGAHgDACMEEEEIAD/BjBD+AEADB+CEAEADB+MEEH8IACBhjBH/AEADCCCEAEADCCMEEP+IACAhjBGAAGADCCDMAEADCCMEEMAIACAhhBCAAGADCCBIAEADCCMEEEAIACBhhBCAACCDCCB4AEADCCMEEEAIAD/Bg/B8AB+DB+AwAEADB+MEHD4IAD4BgAAAAAADAAAwAEADAAMEAAAIAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAFzEPdK0OEUMAAAAAElFTkSuQmCC'
import base64
with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(img_data))
c = Image.open("imageToSave.png")
d = c.resize((1000,700), resample=Image.BOX)
d.show()

'''


