#!/usr/bin/env python
import datetime
from multiprocessing import Process
import sys
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

def displayTheme(file):
    themes = getThemeList()
    print(f'theme: {file}')
    if file in themes:
        print(get_theme(file))
        pattern = get_theme(file)["pattern"]
        if pattern == 'solid':
            SolidColor(file)
        elif pattern == '2Color':
            TwoColorAlter(file)
        elif pattern == '3Color':
            ThreeColorAlter(file)
    if file == 'off':
        off()
        
def SolidColor(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'solid':
        color = get_theme(file)["color1"]
        print(f"1,1,{color}#")
        for i in range(100):
            print(f"1,{i},{color}#")
            port.write(str.encode(f"1,{i},{color}#"))
            port.write(str.encode("show1#"))
            time.sleep(.01)
        
    
    
def TwoColorAlter(file):
    pattern = get_theme(file)["pattern"]
    if pattern == '2Color':
        color1 = get_theme(file)["color1"]
        color2 = get_theme(file)["color2"]
        step = int(get_theme(file)["numPerGroup"])
        for i in range(0, 140, step ):
            for j in range(i, i+step):
                port.write(str.encode(f"1,{i+j},{color1}#"))
                port.write(str.encode("show1#"))
                time.sleep(.01)        
            for j in range(i+step, i+step+step):
                port.write(str.encode(f"1,{i+j},{color2}#"))
                port.write(str.encode("show1#"))
                time.sleep(.01)
        
        
def ThreeColorAlter(file):
    pattern = get_theme(file)["pattern"]
    if pattern == '3Color':
        color1 = get_theme(file)["color1"]
        color2 = get_theme(file)["color2"]
        color3 = get_theme(file)["color3"]
        step = int(get_theme(file)["numPerGroup"])
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
    port.write(str.encode("clear1#"))  
    port.write(str.encode("show1#"))
    
        
def custom(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'custom':
        ...

if __name__ == '__main__':
    # TwoColorAlter('tmp')
    # SolidColor('solidtmp')
    pass