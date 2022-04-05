import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def calculating(temp):
    res = 0
    for i in range(8):
        res += temp[i]/(2**(i+1))
    return res*3.3


dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        temp = input()
        if temp == 'q':
            break
        else:
            temp = int(temp) 
        if temp > 256:
            print('incorrect input value upper 255,', temp)
        temp = decimal2binary(temp)
        for i in range(8):
            GPIO.output(dac[i], temp[i])
        print(calculating(temp))
except ValueError:
    if type(temp) != int:
        print('incorrect input type,', type(temp))
    elif temp < 0:
        print('incorrect input value under zero,', temp)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()