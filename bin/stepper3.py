#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#    Stepper Motor Test
#
# A simple script to control
# a stepper motor.
#
# Author : Matt Hawkins
# Date   : 28/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM) 

# Define GPIO signals to use
# Physical pins 35, 40, 38, 36
# GPIO24, GPIO29, GPIO28, GPIO27
StepPins = [5,6,13,19]

# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False) #set pins low

# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
       
StepCount = len(Seq) #this is an integer of 8 for our purposes

StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

# Read wait time from command line
if len(sys.argv)>2:
   WaitTime = int(sys.argv[1])/float(1000)
   DegRange = float(sys.argv[2])
elif len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
  DegRange = 2048
else:
  WaitTime = 10/float(1000)
  DegRange = 2048


if DegRange < 0:
    StepDir = -1 #acw ie. a negative input from gda
else:
    StepDir = 1 #clockwise ie. positive

# Initialise variables
StepCounter = 0
DegCounter=0

# Start main loop
while True:

  print StepCounter,
  print Seq[StepCounter]
  print DegCounter

  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      #print " Enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir
  DegCounter += StepDir
  if StepDir == -1:
      if (DegCounter<=DegRange):
          break
      else:
          pass
  elif (DegCounter>=DegRange):
          break
  

  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir
    
    

  # Wait before moving on
  time.sleep(WaitTime)
GPIO.cleanup()