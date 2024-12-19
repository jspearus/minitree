#!/usr/bin/env python
import datetime
from multiprocessing import Process
import sys
import threading
import os
import time
import platform
import serial
from serial.serialutil import Timeout
from theme_handler import get_theme
from config import get_config
# for pi zero
port = serial.Serial("/dev/serial0", baudrate=115200, timeout=3.0)
# for pi 4
# port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

def getThemeList():
    config = get_config()
    file_path = config['FILE_PATH']
    folder_path = f'{file_path}themes/'
    files = os.listdir(folder_path)
    themes = []
    for file in files:
        themes.append(file.split('.')[0])
    return themes

def update_config():
    global autoMode, ledType
    config = get_config()
    autoMode = config['auto_mode']
    ledType = config['led_type']
    print(f"auto Mode: {autoMode}")

def convert2rgb(file, key):
    global ledType
    update_config()
    color = file[key]
    color = color[1:] if len(color) > 1 else ""
    colors = []
    dec_colors = []
    print(f'old color: {color}')
    for i in range(0, len(color), 2):
        colors.append(color[i:i+2])
    for color in colors:
        color = int(color, 16)
        dec_colors.append(color)
    print(f'type: {ledType}')
    if ledType == 'rgb':
        color = f"{dec_colors[0]},{dec_colors[1]},{dec_colors[2]}"
    elif ledType == 'grb':
        color = f"{dec_colors[1]},{dec_colors[0]},{dec_colors[2]}"
    print(f"new color: {color}")
    return color
    

def displayTheme(file):
    themes = getThemeList()
    if file == 'off':
        off()
    elif file in themes:
        print(get_theme(file))
        theme = get_theme(file)
        if theme['pattern'] == 'solid':
            SolidColor(convert2rgb(theme, 'color1'))
            
        elif theme['pattern'] == '2Color':
            TwoColorAlter(convert2rgb(theme, 'color1'), convert2rgb(theme, 'color2'), 
                          int(theme['numPerGroup']))
            
        elif theme['pattern'] == '3Color':
            ThreeColorAlter(convert2rgb(theme, 'color1'), convert2rgb(theme, 'color2'), 
                          convert2rgb(theme, 'color3'), int(theme['numPerGroup']))
        print(f"new: {theme}")
        
def SolidColor(color):
    for i in range(140):
        port.write(str.encode(f"1,{i},{color}#"))
        port.write(str.encode("show1#"))
        time.sleep(.01)
        
    
    
def TwoColorAlter(color1, color2, step):
   
    for i in range(0, 140, step ):
        for j in range(i, i+step):
            port.write(str.encode(f"1,{i+j},{color1}#"))
            port.write(str.encode("show1#"))
            time.sleep(.01)        
        for j in range(i+step, i+step+step):
            port.write(str.encode(f"1,{i+j},{color2}#"))
            port.write(str.encode("show1#"))
            time.sleep(.01)
    
        
def ThreeColorAlter(color1, color2, color3, step):
    for i in range(0, 140, step*3):
        for j in range(i, i+step):
            port.write(str.encode(f"1,{j},{color1}#"))
            port.write(str.encode("show1#"))
            time.sleep(.01)       
        for k in range(i+step, i+step+step):
            port.write(str.encode(f"1,{k},{color2}#"))
            port.write(str.encode("show1#"))
            time.sleep(.01)
        for l in range(i+step+step, i+step+step+step):
            port.write(str.encode(f"1,{l},{color3}#"))
            port.write(str.encode("show1#"))
            time.sleep(.01)

        
        
def off():
    for i in range(140, -1, -1):
        port.write(str.encode(f"1,{i},0,0,0#"))
        port.write(str.encode("show1#"))
        time.sleep(.01)
    

if __name__ == '__main__':
    # TwoColorAlter('tmp')
    # SolidColor('solidtmp')
    pass