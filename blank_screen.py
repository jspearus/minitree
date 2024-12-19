#!/usr/bin/env python

import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from ctrl import off

numb = 1
RST = None

# Create the SSD1306 OLED class.
# The first two parameters are the width and height. The third is the I2C interface.
oled = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
# Initialize library.
oled.begin()




def blankScreen():
    # Clear display.
    off()
    off()
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
    padding = 10
    top = padding
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = 0


    # Load default font.
    font = ImageFont.load_default()
    
    # Display image.
    oled.image(image)
    oled.display()

if __name__ == '__main__':
    blankScreen()