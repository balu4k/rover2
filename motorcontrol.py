import time


def stop(GPIO):
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)


def forward(GPIO):
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)


def reverse(GPIO):
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)


def left(GPIO):
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)


def right(GPIO):
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)

def changespeed(GPIO, percent):
    pwm7 = GPIO.PWM(7, 100)
    pwm11 = GPIO.PWM(11, 100)
    pwm13 = GPIO.PWM(13, 100)
    pwm15 = GPIO.PWM(15, 100)
    pwm7.ChangeDutyCycle(percent)
    pwm11.ChangeDutyCycle(percent)
    pwm13.ChangeDutyCycle(percent)
    pwm15.ChangeDutyCycle(percent)

def start(GPIO, percent):
    pwm7 = GPIO.PWM(7, 100)
    pwm11 = GPIO.PWM(11, 100)
    pwm13 = GPIO.PWM(13, 100)
    pwm15 = GPIO.PWM(15, 100)
    pwm7.start(percent)
    pwm11.start(percent)
    pwm13.start(percent)
    pwm15.start(percent)





def test_motor(gpio):
    try:
        for dc in range(0, 3, 1):
            forward(gpio)
            time.sleep(3)

            stop(gpio)
            time.sleep(1)

            reverse(gpio)
            time.sleep(3)

            stop(gpio)
            time.sleep(1)

            left(gpio)
            time.sleep(3)

            stop(gpio)
            time.sleep(1)

            right(gpio)
            time.sleep(3)

            stop(gpio)
            time.sleep(1)
    finally:
        gpio.cleanup()
