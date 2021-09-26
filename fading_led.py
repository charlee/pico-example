from board import *
import pwmio
import time

led = pwmio.PWMOut(LED, frequency=5000, duty_cycle=0)

while True:
    for duty in range(0, 65535, 1000):
        led.duty_cycle = duty
        time.sleep(0.01)

    for duty in range(65535, 0, -1000):
        led.duty_cycle = duty
        time.sleep(0.01)

