from board import *
from digitalio import DigitalInOut, Pull
from time import sleep

button = DigitalInOut(GP14)
button.pull = Pull.DOWN

while True:
    if button.value:
        print("You pressed the button!")
        sleep(2)
