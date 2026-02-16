#Write your code here to run the stepper motor without using any loop
from machine import Pin
import time

coilA = Pin(5, Pin.OUT)
coilB = Pin(18, Pin.OUT)
coilC = Pin(19, Pin.OUT)
coilD = Pin(22, Pin.OUT)

while True:
    
    coilA.value(1)
    coilB.value(0)
    coilC.value(0)
    coilD.value(0)
    time.sleep_us(5)

    coilA.value(0)
    coilB.value(1)
    coilC.value(0)
    coilD.value(0)
    time.sleep_us(5)

    coilA.value(0)
    coilB.value(0)
    coilC.value(1)
    coilD.value(0)
    time.sleep_us(5)

    coilA.value(0)
    coilB.value(0)
    coilC.value(0)
    coilD.value(1)
    time.sleep_us(5)
