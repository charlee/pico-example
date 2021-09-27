from time import sleep
from board import *
from digitalio import DigitalInOut
from sevenseg.TM1637 import TM1637

sevenseg = TM1637(clk=GP17, dio=GP16)

buzzer = DigitalInOut(GP15)
buzzer.switch_to_output()

while True:
    buzzer.value = True
    sleep(0.5)
    buzzer.value = False
    sleep(0.5)
    counter = 20
    while counter > 0:
        counter -= 1
        sevenseg.number(counter)
        if counter < 3:
            buzzer.value = True
            sleep(0.1)
            buzzer.value = False
            sleep(0.9)
        else:
            sleep(1)

    buzzer.value = True
    sleep(0.1)
    buzzer.value = False
    sleep(0.1)
    buzzer.value = True
    sleep(0.1)
    buzzer.value = False
    sleep(0.7)

    counter = 5
    while counter > 0:
        counter -= 1
        sevenseg.number(counter)
        if counter < 3:
            buzzer.value = True
            sleep(0.1)
            buzzer.value = False
            sleep(0.9)
        else:
            sleep(1)


