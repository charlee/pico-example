from board import *
import analogio
import time

potentiometer = analogio.AnalogIn(GP26)

while True:
    print(potentiometer.value)
    time.sleep(1)

