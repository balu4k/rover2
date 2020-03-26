import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


for x in range(0,100):
    print("Starting the program now")
    GPIO.output(7, True)
    print("Lights 1 on")
    time.sleep(.1)

    GPIO.output(7, False)
    GPIO.output(11, True)
    print("Lights 2 on")
    time.sleep(.1)
    GPIO.output(11, False)
    GPIO.output(13, True)
    print("Lights 3 on")
    time.sleep(.1)
    GPIO.output(13, False)
    print("all Lights off")
    time.sleep(.1)

GPIO.cleanup()

