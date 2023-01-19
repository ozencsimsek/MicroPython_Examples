# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

push_button = Pin(13, Pin.IN)  # 23 number pin is input

while True:
  
  logic_state = push_button.value()
  if logic_state == True:     # if pressed the push_button
      oled_width = 128
      oled_height = 64
      oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
      oled.text('Hello, World 1!', 0, 0)
      oled.text('Hello, World 2!', 0, 10)
      oled.text('Ozenc!', 0, 30)
      oled.show()
else:                       # if push_button not pressed
          oled.text('Ozencccc!', 0, 30)
          oled.show()