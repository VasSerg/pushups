import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comparator = 4
troykaModul = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(troykaModul, GPIO.OUT, initial=GPIO.HIGH)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

try:
    while True:
        mem = [0 for _ in range(8)]
        for i in range(bits):
            #mem[bits-1-i] = 1
            mem[i] = 1
            GPIO.output(dac, mem)
            time.sleep(0.07)
            compv = GPIO.input(comparator)
            if compv == 1:
                mem[i] = 0
            print("ADC = {}".format(mem))
        volt = i / levels * maxVoltage
        print("ADC = {}, input voltage = {:.2f}".format(mem,volt))
        
except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
else:
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")