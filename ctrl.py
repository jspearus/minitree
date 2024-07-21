#!/usr/bin/env python
import serial
import time

pixel1 = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        pixel1.write(b'writing...\n')
        print('sent...')
        time.sleep(1)