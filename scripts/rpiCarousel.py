from gda.device.scannable import ScannableBase

import time
from org.slf4j import LoggerFactory
import subprocess
import os

logger = LoggerFactory.getLogger(__name__ + '.py')

class rpiCarousel(ScannableBase):
    def __init__(self, name):
        print "constructing carousel"
        self.setName(name)                                         # required
        self.setInputNames(["Angle"])                       # required
        self.setExtraNames([])      # required
        self.setOutputFormat(["%f"])    # required
        self.currentPosition = 0
        logger.debug("Init of RPi Scannable Completed Successfuly")

    def isBusy(self):
        return False

    def getFormattedPosition(self):
        return self.getPosition()

    def getPosition(self):
        return self.currentPosition


    def asynchronousMoveTo(self,new_position):
        print "moving carousel from ",self.currentPosition, "to ", new_position
        degreesMove = int(new_position) - int(self.currentPosition)
        print "degreesMove: " + str(degreesMove)
        stepsMove = float(4096)/float(360)*float(degreesMove)*float(6.66667)
        print "stepsMove: " + str(stepsMove)
        os.system("python /home/pi/testscripts/stepper2.py " + "2 " + str(stepsMove))
        
        self.currentPosition = self.currentPosition + degreesMove
        

    def sampleCarousel(self,sample):      
        if sample==1 or sample==6:
            self.asynchronousMoveTo(0)
        elif sample==2 or sample==7:
            self.asynchronousMoveTo(72)
        elif sample==3 or sample==8:
            self.asynchronousMoveTo(144)
        elif sample==4 or sample==9:
            self.asynchronousMoveTo(-144)
        elif sample==5 or sample==10:
            self.asynchronousMoveTo(-72)        
        else:
            print("Sample value " + sample + " out of range")
