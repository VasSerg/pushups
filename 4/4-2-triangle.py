import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        period = int(input())
        sleep_time = period/512
        for i in range(256): 
            temp = decimal2binary(i)   
            for j in range(8):
                GPIO.output(dac[j], temp[j])
            time.sleep(sleep_time)
        for i in range(255, 0, -1):
            temp = decimal2binary(i)   
            for j in range(8):
                GPIO.output(dac[j], temp[j])
            time.sleep(sleep_time)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()