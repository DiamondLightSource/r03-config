#!/usr/bin/python

from picamera import PiCamera
from os import system
from time import sleep
from subprocess import call

camera = PiCamera()
camera.resolution = (320, 240)


for i in range(30):
    camera.capture("/home/pi/testscripts/image{0:04d}.jpg".format(i))
    sleep(0.25)


system("convert -delay 100 -loop 0 /home/pi/testscripts/image*.jpg /home/pi/testscripts/animation.gif")
system("convert -delay 100 -loop 0 /home/pi/testscripts/image*.jpg /home/pi/testscripts/image*.gif")

cmd = 'gifsicle --delay=5 -loop 0 --colors 256 /home/pi/testscripts/image*.gif > /home/pi/testscripts/video.gif'
call ([cmd], shell=True)
print("done")
