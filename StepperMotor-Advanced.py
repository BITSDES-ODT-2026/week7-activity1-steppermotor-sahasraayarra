from machine import Pin
import time

coilA = Pin(5, Pin.OUT)
coilB = Pin(18, Pin.OUT)
coilC = Pin(19, Pin.OUT)
coilD = Pin(22, Pin.OUT)

list = [(1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1) ]

while True:
    for step in list:
        coilA.value(step[0])
        coilB.value(step[1])
        coilC.value(step[2])
        coilD.value(step[3])
        time.sleep_ms(5)

