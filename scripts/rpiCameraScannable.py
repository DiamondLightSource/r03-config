from gda.device.detector import DetectorBase
from gda.configuration.properties import LocalProperties
import gda.data as data
from gda.jython import InterfaceProvider
#import rpiComms
import time
import subprocess
import os
from org.slf4j import LoggerFactory

logger = LoggerFactory.getLogger(__name__ + '.py')

class rpiCameraScannable(DetectorBase):
    ## scan info - ScanInformation scanInfo = InterfaceProvider.getCurrentScanInformationHolder().getCurrentScanInformation();
    def __init__(self, name): #setup stuff
        logger.debug("Camera Setup")
        #self.pin = -1 
        self.device = name
        self.setName(name) #this is setting up the name passed in localstation.py
        self.currentPosition = 0
        self.lastPosition = 0                                         # required
        self.busyStatus = False
        beamlineName = LocalProperties.get("gda.beamline.name")
        self.numTracker = data.NumTracker(beamlineName)
        print "camera setup"
       # rpiComms.rpiCommunicator.scannables.append(self)
        
            
    def collectData(self):
        self.busyStatus = True
        self.lastPosition = self.currentPosition
       # rpiComms.commController.outgoingQueue.put("-1,c"+self.device+",CAPTURE,None,0//")
        os.system("python3 /home/pi/testscripts/gdacamera.py " + self.datFile + "/%s-%04i" % (self.current_scan, self.frameNum))
        self.frameNum += 1
    
    def readout(self):
        return self.currentPosition
    
    def waitWhileBusy(self):
        #while (self.busyStatus == True):
            #if (self.lastPosition == self.currentPosition):
                #time.sleep(0.1)
            #else:
                #self.busyStatus = False
        pass

    def atScanStart(self): #find out where to save pictures
        num = self.numTracker.getCurrentFileNumber() #scan number into var "num"
        self.datFile = data.PathConstructor.getVisitSubdirectory(str(num))
        self.frameNum = 0
        logger.debug("CAM DAT NAME =" + self.datFile)
        logger.debug("NUM =" + str(num))
        os.mkdir(self.datFile)
        self.current_scan=num
#        self.datFile = self.datFile + "/" + str(num)
        logger.debug(self.datFile) 
        self.datFile = self.datFile.replace("//", "/")
        logger.debug(self.datFile)
        dirs = self.datFile.split("/") #getting a list of dirs in path
        cleanPath = []
        for dir in dirs: 
            logger.trace("DIR = "+ dir)
            if dir == "..": #this loop cleans up the path incase eg. full of /../ in path
                cleanPath.pop()
            else:
                cleanPath.append(dir)
        self.datFile = "/".join(cleanPath) #so self.datFile is where we want to write to
        logger.debug(self.datFile)
        print self.datFile
       # rpiComms.commController.outgoingQueue.put("-1,c"+self.device+",START,"+self.datFile+","+str(num)+"//")
        
    