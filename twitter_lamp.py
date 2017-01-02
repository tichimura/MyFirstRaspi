#!/usr/bin/env python

import tweepy
import random, time
import RPi.GPIO as GPIO

api_key = '79Ey99baEGDcs1KS3j8hNNdkj' 
api_secret = '1xkIovgMgvXpyvLcCxUySwJlMp2STiF6Y14MunSeZHW9QT98Ad' 
access_token = '264774670-fNl3JPv2vwmjdmUDra1v88U327i4E14j6MSieRA5'
token_secret = '4Ms8CKxqp3SLqjsKhnyCO8xCfgezURXw0RUYSfWTKQcsi' 

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)
my = api.me()

print my.name, "is connected! Press CTRL+C to quit."

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# Set the LED light to be 'on'
# in candle_light, we use PWM 
GPIO.output(led, GPIO.HIGH)

class StreamListener(tweepy.StreamListener):

 # in candle_light, we use pwm.ChangeDutyCycle
 def on_status(self, data):
   print "Flash the light"
   for i in xrange(3):
     GPIO.output(led, GPIO.LOW)
     time.sleep(0.25)
     GPIO.output(led, GPIO.HIGH)
     time.sleep(0.25)
 
 def on_error(self, error_code):
   print "Error:", error_code
   return False

terms = ['raspberry pi', 'raspberrypi', 'raspi']

# try-error-finally loop
# don't forget for the GPIO next time.

try:
  listener = StreamListener()
  stream = tweepy.Stream(auth, listener)
  stream.filter(track = terms)

except KeyboardInterrupt:
  print "\nQuitting"

finally:
  GPIO.cleanup()
