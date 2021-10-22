import random
import time
from board import *
from digitalio import DigitalInOut, Pull

led = DigitalInOut(GP15)
led.switch_to_output()
left_button = DigitalInOut(GP14)
left_button.pull = Pull.DOWN
right_button = DigitalInOut(GP16)
right_button.pull = Pull.DOWN

# LED on
led.value = True

# sleep for a random period of time
time.sleep(random.randint(2, 5))

# LED off
led.value = False

# record current timer
ticks = time.monotonic()

# print a message when the button is pressed
while True:
    if left_button.value or right_button.value:
        if left_button.value:
            print("Left player win!")
        else:
            print("Right player win!")
        break
    time.sleep(0.01)
