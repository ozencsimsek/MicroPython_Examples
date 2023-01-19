from machine import Pin
import time
p5=Pin(45,Pin.IN)
p4=Pin(40,Pin.OUT, value=0)
butonDurum=0
counter=0
def callback(p):
 print("Interrupt funtion is working...",p)
p5.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=callback)
while True:
    p4.on()
    print("Led is on")
    time.sleep(0.2)
    p4.off()
    print("Led is off")
    time.sleep(0.2)