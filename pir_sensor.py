from machine import Pin       #importing classes
from time import sleep    #Import sleep from time class

Motion_Detected = False  #Global variable to hold the state of motion sensor

def handle_interrupt(Pin):           #defining interrupt handling function
 global Motion_Detected
 Motion_Detected = True

led=Pin(14,Pin.OUT)   #setting GPIO14 led as output
PIR_Interrupt=Pin(13,Pin.IN)   # setting GPIO13 PIR_Interrupt as input

#Attach external interrupt to GPIO13 and rising edge as an external event source
PIR_Interrupt.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)        

while True:
  if Motion_Detected:
   print('Motion is detected!')
   led.value(1)
   sleep(20)
   led.value(0)
   print('Motion is stopped!')
   Motion_Detected = False
  else:
   led.value(1)    #led is on
   sleep(1)        #delay of 1 second
   led.value(0)    #led is off
   sleep(1)        #delay of 1 second