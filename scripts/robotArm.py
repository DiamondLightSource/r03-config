from gda.device.scannable import ScannableBase
import socket
import time
from org.slf4j import LoggerFactory
import subprocess
import os
from time import sleep

#positions:
HOME = (150,0,150)

LOWER_OUT = (90,100,53)
LOWER_ON = (123,133,53)
LOWER_UP = (123,133,74)
LOWER_BACK = (90,100,74)

UPPER_OUT= (94,99,140)
UPPER_ON = (124,131,154)
UPPER_UP = (122,128,165)
UPPER_BACK = (94,99,140)

MIDWAY = (138,86,69)

TABLE_REF_1 = (219,90,47)
UPPER_TABLE = (248,104,47)
LOWER_TABLE = (248,104,32)
TABLE_REF_2 = (203,90,32)

logger = LoggerFactory.getLogger(__name__ + '.py')

class robotArm(ScannableBase):
    def __init__(self, name):
        self.sock=socket.socket()
        self.sock.connect(("localhost",4446))
        print "arm comm set up"

        self.lower_sample = HOME, LOWER_OUT , None, LOWER_ON , LOWER_UP , LOWER_BACK , MIDWAY, TABLE_REF_1, UPPER_TABLE, LOWER_TABLE, TABLE_REF_2, HOME
        self.upper_sample = HOME, UPPER_OUT , None, UPPER_ON , UPPER_UP , UPPER_BACK , MIDWAY, TABLE_REF_1, UPPER_TABLE, LOWER_TABLE, TABLE_REF_2, HOME
        
        self.setName(name)                                         
        self.setInputNames(["Sample"])                      
        self.setExtraNames([])      
        self.setOutputFormat(["%f"])    
        self.currentPosition = 0
        logger.debug("Init of Robot Arm Completed Successfully")

    def isBusy(self):
        return False

    def move_to_xyz(self,x,y,z,speed=10000):
        self.sock.send('{{"func": "set_position", "args": [{}, {}, {}, {}]}}\n'.format(x,y,z,speed))
        print(self.sock.recv(1024))
        
    def wrist(self,deg,speed=100):
        self.sock.send('{{"func": "set_wrist", "args": [{}, {}]}}\n'.format(deg,speed))
        print(self.sock.recv(1024))

    def moveSequence(self,args):     
        for pos in args:
            print pos
            if pos==None:
                sleep(1)
            elif len(pos)==1:
                print pos[0]
                self.wrist(pos[0])
            else:
                self.move_to_xyz(*pos)
        
    def loadSample(self,sample):
        self.wrist(85)
        if sample>5 and sample<11:
            print("going to need to run some script that rotates the sample carousel to pos(sample)")
            self.moveSequence(self.upper_sample)
        elif sample<6 and sample>0:
            print("going to need to run some script that rotates the sample carousel to pos(sample)")
            self.moveSequence(self.lower_sample)
        else:
            print("Sample value " + sample + " out of range")
        

    def unloadSample(self,sample):      
        if sample>5 and sample<11:
            self.moveSequence(self.upper_sample[::-1])
        elif sample<6 and sample>0:
            self.moveSequence(self.lower_sample[::-1])





        
