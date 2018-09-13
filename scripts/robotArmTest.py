from gda.device.scannable import ScannableBase
import socket
import time
from org.slf4j import LoggerFactory
import subprocess
import os
from time import sleep

logger = LoggerFactory.getLogger(__name__ + '.py')

class robotArm(ScannableBase):
    def __init__(self, name):
        print "setting up arm comm"
        self.sock=socket.socket()
        self.sock.connect(("localhost",4446))
        
        self.setName(name)                                         # required
        self.setInputNames(["Sample"])                       # required
        self.setExtraNames([])      # required
        self.setOutputFormat(["%f"])    # required
        self.currentPosition = 0
        logger.debug("Init of Robot Arm Completed Successfully")

    def isBusy(self):
        return False

    def move_to_xyz(self,x,y,z,speed=10000):
        self.sock.send('{{"func": "set_position", "args": [{}, {}, {}, {}]}}\n'.format(x,y,z,speed))
        print(self.sock.recv(1024))
        
    def wrist(self,deg,speed=1000):
        self.sock.send('{{"func": "set_wrist", "args": [{}, {}]}}\n'.format(deg,speed))
        print(self.sock.recv(1024))


    def lowerSample(self):
        self.move_to_xyz(150,0,150) #awake but inactive position
        self.wrist(10)
        sleep(1)
        self.move_to_xyz(100,-200,30)
        sleep(1)
        self.move_to_xyz(100,-230,30,1000)
        sleep(2)
        self.move_to_xyz(100,-230,50,1000)
        sleep(2)
        self.move_to_xyz(290,-150,50)
        self.wrist(100)
        sleep(1)
        self.move_to_xyz(310,-150,40,1000)
        sleep(3)
        self.move_to_xyz(275,-150,40,1000)
        self.move_to_xyz(150,0,150)
        
    def upperSample(self):
        self.move_to_xyz(150,0,150) #awake but inactive position
        self.wrist(10)
        sleep(1)
        self.move_to_xyz(100,-200,130)
        sleep(1)
        self.move_to_xyz(100,-230,130,1000)
        sleep(2)
        self.move_to_xyz(100,-230,150,1000)
        sleep(2)
        self.move_to_xyz(290,-150,150)
        self.wrist(100)
        sleep(1)
        self.move_to_xyz(310,-150,40,1000)
        sleep(3)
        self.move_to_xyz(275,-150,40,1000)
        self.move_to_xyz(150,0,150)
        
    def loadSample(self,sample):      
        if sample>5:
            print("going to need to run some script that rotates the sample carousel to pos(sample)")
            self.upperSample()
        elif sample<6:
            print("going to need to run some script that rotates the sample carousel to pos(sample)")
            self.lowerSample()
        else:
            print("Sample value " + sample + " out of range")