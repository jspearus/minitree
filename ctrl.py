#!/usr/bin/env python
import serial
import os
import time
from smbus2 import SMBus
from json_handler import get_theme

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

# pixel1 = serial.Serial(
#         port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
#         baudrate = 115200,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#         timeout=1
# )
def getThemeList():
    folder_path = 'themes/'
    files = os.listdir(folder_path)
    themes = []
    for file in files:
        themes.append(file.split('.')[0])
    return themes

def displayTheme(file):
    themes = getThemeList()
    if file in themes:
        pattern = get_theme(file)["pattern"]
        if pattern == 'solid':
            SolidColor(file)
        elif pattern == 'multicolor':
            TwoColorAlter(file)
        
def SolidColor(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'solid':
        color = get_theme(file)["color"]
        for i in range(37):
            data = f",1,{i},{color}"
            msg = list(data.encode('ascii'))
            bus.write_i2c_block_data(addr, 10, msg)
            time.sleep(.001)
        data = "show1"
        msg = list(data.encode('ascii'))
        bus.write_i2c_block_data(addr, 10, msg)  
    
def TwoColorAlter(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'multicolor':
        color1 = get_theme(file)["color 1"]
        color2 = get_theme(file)["color 2"]
        step = get_theme(file)["numPerGroup"]
        for i in range(0, 37, step ):
            for j in range(i, i+step):
                data = f",1,{i+j},{color1}"
                msg = list(data.encode('ascii'))
                bus.write_i2c_block_data(addr, 10, msg)
                time.sleep(.001)
            for j in range(i+step, i+step+step):
                data = f",1,{i+j},{color2}"
                msg = list(data.encode('ascii'))
                bus.write_i2c_block_data(addr, 10, msg)
                time.sleep(.001)
        data = "show1"
        msg = list(data.encode('ascii'))
        bus.write_i2c_block_data(addr, 10, msg)
        
def off():
    data = "clear1"
    msg = list(data.encode('ascii'))
    bus.write_i2c_block_data(addr, 10, msg)
    time.sleep(.001)
    data = "show1"
    msg = list(data.encode('ascii'))
    bus.write_i2c_block_data(addr, 10, msg)
        
def custum(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'custom':
        ...
    
if __name__ == '__main__':
    # TwoColorAlter('tmp')
    # SolidColor('solidtmp')
    pass