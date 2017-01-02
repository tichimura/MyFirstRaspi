#!/usr/bin/env python

import random, time
import RPi.GPIO as GPIO

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 100)
RUNNING = True
WIND = 9

def brightness():
	"""Function to randomly set the brightness of the LED between 5 per cent and 100 per cent power"""
	return random.randint(5, 100)

def flicker():
	"""Function to randomly set the regularity of the 'flicker effect'"""
	return random.random() / WIND

print "Candle Light. Press CTRL + C to quit"

try:
	while RUNNING:
		pwm.start(0)
		pwm.ChangeDutyCycle(brightness())
		time.sleep(flicker())

except KeyboardInterrupt:
	running = False
	print "\Quitting Candle Light"

finally:
	pwm.stop()
	GPIO.cleanup()
