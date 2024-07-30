#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com
 
from smbus2 import SMBus
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess


 
numb = 1
RST = None



# Create the SSD1306 OLED class.
# The first two parameters are the width and height. The third is the I2C interface.
oled = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
# Initialize library.
oled.begin()

# Clear display.
oled.clear()
oled.display()


# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = oled.width
height = oled.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

 # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
CPU = subprocess.check_output(cmd, shell = True )
cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
MemUsage = subprocess.check_output(cmd, shell = True )
cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
Disk = subprocess.check_output(cmd, shell = True )

# Write two lines of text.

draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
draw.text((x, top+8),     str(CPU), font=font, fill=255)
draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)
draw.text((x, top+25),    str(Disk),  font=font, fill=255)
# Display image.
oled.image(image)
oled.display()

 
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
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