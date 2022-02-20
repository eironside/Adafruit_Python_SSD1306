# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
import i2c_mux 
i2c_mux.set_chan(i2c_mux.RIGHT_MUX,0)
MAX_IMAGES=1

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# an array of arrays: [side, channel, disp, filename]
displays = [
            [i2c_mux.RIGHT_MUX, 2, Adafruit_SSD1306.SSD1306_128_64(rst=RST7)],
            [i2c_mux.RIGHT_MUX, 3, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.RIGHT_MUX, 4, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.RIGHT_MUX, 5, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.RIGHT_MUX, 6, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.RIGHT_MUX, 7, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.LEFT_MUX, 2, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.LEFT_MUX, 4, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.LEFT_MUX, 5, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.LEFT_MUX, 6, Adafruit_SSD1306.SSD1306_128_64(rst=RST)],
            [i2c_mux.LEFT_MUX, 7, Adafruit_SSD1306.SSD1306_128_64(rst=RST)]
           ]


# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

for side, channel, disp, file_name in displays:
    i2c_mux.set_chan(side,channel)
    # Initialize library.
    disp.begin()

    # Clear display.
    disp.clear()
    disp.display()

# Load image based on OLED display height.  Note that image is converted to 1 bit color.
# if disp.height == 64:
#     image = Image.open('happycat_oled_64.ppm').convert('1')
# else:
#     image = Image.open('happycat_oled_32.ppm').convert('1')

# Alternatively load a different format image, resize it, and convert to 1 bit color.
#image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')


# Display image.
# disp.image(image)
# disp.display()

# loop through 10 sets of images (if they exist)
for image_num in range(0,MAX_IMAGES):
    for side, channel, disp, file_name in displays:
        i2c_mux.set_chan(side,channel)

        # construct the image name converting image_num and channel to strings first
        image_file = file_name+str(image_num)+'_'+str(channel)+".ppm"
        
        # check if the image file exists
        if path.exists(path.join('.',image_file)):
            image = Image.open(image_file).convert('1')
            disp.image(image)
            disp.display()

