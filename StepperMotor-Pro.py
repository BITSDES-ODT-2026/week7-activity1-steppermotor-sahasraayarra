from machine import Pin
import time

coilA = Pin(5, Pin.OUT)
coilB = Pin(18, Pin.OUT)
coilC = Pin(19, Pin.OUT)
coilD = Pin(22, Pin.OUT)

m_list = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1) ]

while True:
    for i in range(1, 500, 1):
        for step in m_list:
            coilA.value(step[0])
            coilB.value(step[1])
            coilC.value(step[2])
            coilD.value(step[3])
            time.sleep_ms(3)
        
    for i in range(1, 500, 1):
        for step in m_list:
            coilA.value(step[3])
            coilB.value(step[2])
            coilC.value(step[1])
            coilD.value(step[0])
            time.sleep_ms(3)
