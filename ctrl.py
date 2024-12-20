#!/usr/bin/env python
import os
import time
from smbus2 import SMBus
from theme_handler import get_theme

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
time.sleep(1)
if not bus:
    bus.open(1)

def getThemeList():
    folder_path = '/home/jeff/minitree/themes/'
    files = os.listdir(folder_path)
    themes = []
    for file in files:
        themes.append(file.split('.')[0])
    return themes

def displayTheme(file):
    themes = getThemeList()
    print(f'theme: {file}')
    if file in themes:
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
        for i in range(140):
            data = f",1,{i},{color}"
            send_data(data)
        data = "show1"
        send_data(data)
    
    
def TwoColorAlter(file):
    pattern = get_theme(file)["pattern"]
    if pattern == '2Color':
        color1 = get_theme(file)["color1"]
        color2 = get_theme(file)["color2"]
        step = int(get_theme(file)["numPerGroup"])
        for i in range(0, 140, step ):
            for j in range(i, i+step):
                data = f",1,{i+j},{color1}"
                send_data(data)
            for j in range(i+step, i+step+step):
                data = f",1,{i+j},{color2}"
                send_data(data)
        data = "show1"
        send_data(data)
        
def ThreeColorAlter(file):
    pattern = get_theme(file)["pattern"]
    if pattern == '3Color':
        color1 = get_theme(file)["color1"]
        color2 = get_theme(file)["color2"]
        color3 = get_theme(file)["color3"]
        step = int(get_theme(file)["numPerGroup"])
        for i in range(0, 140, step*3):
            for j in range(i, i+step):
                data = f",1,{j},{color1}"
                send_data(data)
            for k in range(i+step, i+step+step):
                data = f",1,{k},{color2}"
                send_data(data)
            for l in range(i+step+step, i+step+step+step):
                data = f",1,{l},{color3}"
                send_data(data)
            
        data = "show1"
        send_data(data)
        
def off():
    data = "clear1"
    send_data(data)
    data = "show1"
    send_data(data)
        
def custom(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'custom':
        ...
        
def send_data(data):
    msg = list(data.encode('ascii'))
    try:
        bus.write_i2c_block_data(addr, 10, msg)
    except Exception as error:
        # handle the exception
        print("An exception occurred:", type(error).__name__) 
        print("message:", error) 
    # bus.close()
if __name__ == '__main__':
    # TwoColorAlter('tmp')
    # SolidColor('solidtmp')
    pass