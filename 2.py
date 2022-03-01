import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM )

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
if GPIO.input(24):
    GPIO.output(23, 1)
else:
    GPIO.output(23, 0)
print(GPIO.input(24))