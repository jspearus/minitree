#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com
 
from smbus2 import SMBus
import time
import board
import busio
import adafruit_ssd1306
 
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
numb = 1
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the width and height. The third is the I2C interface.
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display.
oled.fill(0)
oled.show()

# Draw some text.
oled.text("Hello, World!", 0, 0, 1)
 
print ("Enter 1 for ON or 0 for OFF")
while numb == 1:
 
    ledstate = input(">>>>   ")

    if ledstate == "1":
        bus.write_byte(addr, 0x1) # switch it on
    elif ledstate == "0":
        bus.write_byte(addr, 0x0) # switch it on
        bus.write_i2c_block_data(addr, 1, [12, 2, 255])
    else:
        numb = 0