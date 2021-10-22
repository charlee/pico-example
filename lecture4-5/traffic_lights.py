from board import *
from digitalio import DigitalInOut
from time import sleep

led_red = DigitalInOut(GP15)
led_amber = DigitalInOut(GP14)
led_green = DigitalInOut(GP13)

led_red.switch_to_output()
led_amber.switch_to_output()
led_green.switch_to_output()

while True:
    led_green.value = True
    led_amber.value = False
    led_red.value = False
    sleep(5)

    led_green.value = False
    led_amber.value = True
    sleep(1)

    led_red.value = True
    led_amber.value = False
    sleep(5)

    led_amber.value = True
    sleep(1)
