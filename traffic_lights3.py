from board import *
from digitalio import DigitalInOut, Pull
from time import sleep

led_red = DigitalInOut(GP15)
led_amber = DigitalInOut(GP14)
led_green = DigitalInOut(GP13)

led_red.switch_to_output()
led_amber.switch_to_output()
led_green.switch_to_output()

button = DigitalInOut(GP16)
button.pull = Pull.DOWN

while True:
    led_green.value = True
    led_amber.value = False
    led_red.value = False

    while not button.value:
        sleep(0.1)

    led_green.value = False
    led_amber.value = True
    sleep(1)

    led_red.value = True
    led_amber.value = False
    for i in range(5):
      buzzer.value = True
      sleep(0.1)
      buzzer.value = False
      sleep(0.9)

    led_amber.value = True
    sleep(1)
