#!/usr/bin/env python

import tweepy
import random, time, os
import RPi.GPIO as GPIO
import picamera

api_key = '79Ey99baEGDcs1KS3j8hNNdkj' 
api_secret = '1xkIovgMgvXpyvLcCxUySwJlMp2STiF6Y14MunSeZHW9QT98Ad' 
access_token = '264774670-fNl3JPv2vwmjdmUDra1v88U327i4E14j6MSieRA5'
token_secret = '4Ms8CKxqp3SLqjsKhnyCO8xCfgezURXw0RUYSfWTKQcsi' 

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)
my = api.me()
tweet_text = ['Another shot taken with mytweet-pi', 'Just spotted with my Raspberry Pi3','Demo for PIR with Camera'] 

print my.name, "is connected! Press CTRL+C to quit."

pir = 17
GPIO.setmode(GPIO.BCM)
# set pir as IN, not OUT
GPIO.setup(pir, GPIO.IN)

### Camera Settings
camera = picamera.PiCamera()
cam_res = (1024, 768)
camera.led = True # False for birds
pics_taken = 0
time.sleep(1)

# MAIN 

def motion_sense(pir):
  print "Motion detected... Taking picture!"
  take_picture(cam_res)

def take_picture(resolution):
  global pics_taken
  camera.resolution = resolution
  camera.capture(os.path.join('pics', 'image_' + str(pics_taken) + '.jpg'))
  pics_taken += 1
  print " Capturing Image, now Tweeting! """
  update_twitter()

def update_twitter():
  api.update_with_media(os.path.join('pics', 'image_' + str(pics_taken -1) + '.jpg'), 
  status = random.choice(tweet_text))
  print " Tweeted! """
  time.sleep(60)

try:
  GPIO.add_event_detect(pir, GPIO.RISING, callback=motion_sense)
  while True:
    time.sleep(60)
except KeyboardInterrupt:
  print "\n Quitting..."

finally:
  camera.close()
  GPIO.cleanup()
