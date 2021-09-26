import random
import time
from board import *
from digitalio import DigitalInOut, Pull

led = DigitalInOut(GP15)
led.switch_to_output()
button = DigitalInOut(GP14)
button.pull = Pull.DOWN

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
    if button.value:
        new_ticks = time.monotonic()
        reaction_time = new_ticks - ticks
        print("Your reaction time is %s seconds!" % reaction_time)
        break
    time.sleep(0.01)

