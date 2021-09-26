import time
import microcontroller

while True:
    print(microcontroller.cpu.temperature)
    time.sleep(1)

