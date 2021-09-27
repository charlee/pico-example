from time import sleep
from board import *
from digitalio import DigitalInOut
from sevenseg.TM1637 import TM1637

sevenseg = TM1637(clk=GP17, dio=GP16)

buzzer = DigitalInOut(GP15)
buzzer.switch_to_output()

def sleep_1s_beep():
    buzzer.value = True
    sleep(0.1)
    buzzer.value = False
    sleep(0.9)
    
def countdown():
    global counter
    while counter > 0:
        counter -= 1
        sevenseg.number(counter)
        if counter < 3:
            sleep_1s_beep()
        else:
            sleep(1)
        
def one_long_beep():
    buzzer.value = True
    sleep(0.5)
    buzzer.value = False
    sleep(0.5)
    
def two_short_beeps():
    buzzer.value = True
    sleep(0.1)
    buzzer.value = False
    sleep(0.1)
    buzzer.value = True
    sleep(0.1)
    buzzer.value = False
    sleep(0.7)
    
while True:
    one_long_beep()
    counter = 20
    countdown()

    two_short_beeps()
    counter = 5
    countdown()


