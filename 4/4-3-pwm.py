import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

try:
    while True:
        duty_cycle = int(input('input duty cycle:'))
        p = GPIO.PWM(22, 1000)
        p.start(duty_cycle)
        time.sleep(10)
        p.stop()
finally:
    p.stop()
    GPIO.cleanup()
