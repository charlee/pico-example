import board
import digitalio
import time

button = digitalio.DigitalInOut(board.GP14)
button.pull = digitalio.Pull.DOWN

while True:
    if button.value == True:
        print("You pressed the button!")
        time.sleep(2)
