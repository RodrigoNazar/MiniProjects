from utime import sleep
from machine import Pin, PWM

# El pin 2 es un led azul

# Pin de Saludo
buitin_led = Pin(2, Pin.OUT)

buitin_led.on()                 # set pin to "on" (high) level
sleep(.3)
buitin_led.off()    

sleep(.1)

buitin_led.on()                 # set pin to "on" (high) level
sleep(.3)
buitin_led.off()    

# PWM
F_MIN = 500
F_MAX = 1000

f = F_MIN
delta_f = 1

p = PWM(Pin(13), f)
print(p)

while True:
    p.freq(f)

    sleep(10 / F_MIN)

    f += delta_f
    if f >= F_MAX or f <= F_MIN:
        delta_f = -delta_f
