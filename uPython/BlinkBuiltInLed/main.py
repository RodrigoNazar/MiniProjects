from machine import Pin
from time import sleep

# Pin de Saludo
buitin_led = Pin(2, Pin.OUT)

buitin_led.on()                 # set pin to "on" (high) level
sleep(.3)
buitin_led.off()    

sleep(.1)

buitin_led.on()                 # set pin to "on" (high) level
sleep(.3)
buitin_led.off()  

# El pin 2 es un led azul

buitin_led = Pin(13, Pin.OUT)

buitin_led.on()                 # set pin to "on" (high) level
buitin_led.off()                # set pin to "off" (low) level

while 1:
    buitin_led.on()                 # set pin to "on" (high) 
    sleep(1)
    buitin_led.off()                # set pin to "off" (low) level
    sleep(1)
