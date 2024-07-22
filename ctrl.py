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

print('running...')
color1 = get_theme('tmp')["color 1"]
color2 = get_theme('tmp')["color 2"]
while 1:
    for i in range(37):
        pixel1.write(str.encode(f"1,{i},{color1}#"))
    pixel1.write(str.encode("show1#"))
    print('sent...')
    time.sleep(1)
    for i in range(37):
        pixel1.write(str.encode(f"1,{i},{color2}#"))
    pixel1.write(str.encode("show1#"))
    time.sleep(1)
    pixel1.write(str.encode("clear1#"))
    pixel1.write(str.encode("show1#"))
    time.sleep(1)