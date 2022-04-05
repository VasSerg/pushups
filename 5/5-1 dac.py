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
        for i in range(256):
            
            sig = num2dac(i)
            time.sleep(0.0007)
            volt = i / levels * maxVoltage
            compv = GPIO.input(comparator)
            if compv == 0:
                print("ADC value = {:.^3} -> {}, input voltage = {:.2f}".format(i,sig,volt))
                break
        
except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")