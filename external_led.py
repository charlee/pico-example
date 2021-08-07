import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP15)
led.switch_to_output()

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)


