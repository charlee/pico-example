import time
from board import *
from digitalio import DigitalInOut, Pull

sensor_pir = DigitalInOut(GP28)
sensor_pir.pull = Pull.DOWN

led = DigitalInOut(GP15)
led.switch_to_output()

buzzer = DigitalInOut(GP14)
buzzer.switch_to_output()

while True:
    if sensor_pir.value:
        print("ALARM! Motion detected!")
        # flash LED quickly
        for i in range(50):
            led.value = not led.value
            buzzer.value = not buzzer.value
            time.sleep(0.1)
        # make sure the buzzer is off
        buzzer.value = False
    # flash LED slowly
    led.value = not led.value
    time.sleep(1)
