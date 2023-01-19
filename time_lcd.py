#Nokia 5110 in Wemos ESP 32
# Pinout
# 3V3 or any Pin => VCC       3.3V logic voltage (0=off, 1=on)
# MOSI (35)      => DIN       data flow (Master out, Slave in)
# SCK  (36)      => CLK       SPI clock
# Pin  (0)       => RST       Reset pin (0=reset, 1=normal)
# Pin  (26)      => CE        Chip Enable (0=listen for input, 1=ignore input)
# Pin  (34)      => DC        Data/Command (0=commands, 1=data)
# Pin  (37)      => LIGHT     Light (0=on, 1=off)
# GND            => GND
# References:  https://github.com/mcauser/micropython-pcd8544
#              http://docs.micropython.org/en/latest/pyboard/library/machine.SPI.html
#              http://pedrominatel.com.br/pt/esp8266/utilizando-o-lcd-nokia-5110-no-esp8266/

import pcd8544
import framebuf
import utime
import machine
import _thread

from machine import Pin, SPI


spi = SPI(1, baudrate=328125, bits=8, polarity=0, phase=1, sck=36, mosi=35, miso=37)

spi.init()
cs = Pin(26)
dc = Pin(34)
rst = Pin(0)

led = Pin(16)

# backlight on
bl = Pin(40, Pin.OUT, value=0)

lcd = pcd8544.PCD8544(spi, cs, dc, rst)
lcd.contrast(0x3c, pcd8544.BIAS_1_40, pcd8544.TEMP_COEFF_0)
lcd.reset()
lcd.init()
lcd.clear()


buffer = bytearray((lcd.height // 8) * lcd.width)
framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)

rtc = machine.RTC()
rtc.ntp_sync ('a.ntp.br')
rtc.init (rtc.now())

def watch():
    data = strftime('%d/%m/%y')
    relogio = strftime('%H:%M:%S')
    lcd.position(0, 0)
    while True:
	framebuf.text(data, 10, 12, 1)
	framebuf.text(relogio,10,24,1)
	lcd.data(buffer)
	agora = strftime('%H:%M:%S')
	
	if relogio != agora:
            relogio = agora	
	    framebuf.fill(0) # clear framebuffer
	    utime.sleep(1)
	    lcd.data(buffer)
	    
_thread.start_new_thread ("clock",watch, ())