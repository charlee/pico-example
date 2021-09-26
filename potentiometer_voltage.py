from board import *
import analogio
import time

potentiometer = analogio.AnalogIn(GP26)

while True:
    voltage = potentiometer.value / 65535 * 3.3
    print(voltage)
    time.sleep(1)

