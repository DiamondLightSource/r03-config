#!/usr/bin/python

from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (320, 240)


for i in range(30):
    camera.capture("/home/pi/testscripts/image{0:04d}.jpg".format(i))
    sleep(0.20)


system("convert -delay 10 -loop 0 /home/pi/testscripts/image*.jpg /home/pi/testscripts/animation.gif")
print("done")
