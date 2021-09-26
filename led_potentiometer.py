from board import *
import analogio
import pwmio
import time

led = pwmio.PWMOut(LED, frequency=5000, duty_cycle=0)
potentiometer = analogio.AnalogIn(GP26)

while True:
    led.duty_cycle = potentiometer.value
    time.sleep(0.1)
