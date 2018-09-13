#!/usr/bin/python

import sys
import os
from picamera import PiCamera
from os import system
from time import sleep


camera = PiCamera()
camera.resolution = (2592,1944)
camera.zoom = (0.2, 0.35, 0.5, 0.5)
#camera.annotate_text = '@DiamondRPi'
print(sys.argv[0])
print(sys.argv[1])

camera.capture(sys.argv[1] + ".jpg")
sleep(0.25)

print('scan saved at ' + sys.argv[1] + '.jpg')
