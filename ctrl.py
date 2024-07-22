#!/usr/bin/env python
import serial
import time
from json_handler import get_theme

pixel1 = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

def SolidColor(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'solid':
        color = get_theme(file)["color"]
        for i in range(37):
            pixel1.write(str.encode(f"1,{i},{color}#"))
        pixel1.write(str.encode("show1#"))   
    
def TwoColorAlter(file):
    pattern = get_theme(file)["pattern"]
    if pattern == '2coloralter':
        color1 = get_theme(file)["color 1"]
        color2 = get_theme(file)["color 2"]
        step = get_theme(file)["numPerGroup"]
        for i in range(0, 37, step ):
            for j in range(i, i+step):
                pixel1.write(str.encode(f"1,{i+j},{color1}#"))
            for j in range(i+step, i+step+step):
                pixel1.write(str.encode(f"1,{i+j},{color2}#"))
        pixel1.write(str.encode("show1#"))
        
def custum(file):
    pattern = get_theme(file)["pattern"]
    if pattern == 'custom':
        ...
    
if __name__ == '__main__':
    # TwoColorAlter('tmp')
    SolidColor('solidtmp')
    pass