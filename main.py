# Emre Guzel
# Feb 11, 2026
# Blink program in Python

import board
import digitalio
import time

#Setting the verible 
blink_time = 1.0  

# Setting the LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#Setting the loop
while True:
    led.value = True
    time.sleep(blink_time)
    
    led.value = False
    time.sleep(blink_time)
    
    blink_time = blink_time + 1.0
    