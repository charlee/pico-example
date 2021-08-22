from board import *
from digitalio import DigitalInOut, Pull
from time import sleep

button = DigitalInOut(GP14)
button.pull = Pull.DOWN

led = DigitalInOut(GP15)
led.switch_to_output()

while True:
    if button.value:
        led.value = True
        sleep(2)

    led.value = False

