''' gdaserver.py: generated by SpringObjectServer.writeFindablesJythonModule

Generated on server start, this Jython module 'gdaserver.py', in each config's
config/scripts directory, acts as a development-time reference for Findable
objects created by Spring XML. This trick enables PyDev auto-completion of
server-side GDA objects and their methods in the IDE and Pythonic import
syntax of multiple device in user scripts, e.g.:

>>> from gdaserver import gripper_x, gripper_grp as gripper_jaws

See Confluence for rationale: http://confluence.diamond.ac.uk/x/IwyvAw

PLEASE DO NOT COMMIT THIS FILE
You should ignore it in: config/scripts/.gitignore

ANY CHANGES WILL BE OVERWRITTEN WITHOUT WARNING

'''

# generation-time attributes
__beamline__ = 'EXAMPLE'
__gdaversion__ = '9.9.0pre'
__xmlfile__ = '/home/pi/server_20180710-1656_linux64/rpi-config/rpi-config/servers/main/dummy/server.xml'
__pid__ = '803'
__hostname__ = 'raspberrypi'
__timestamp__ = '2018-09-13 09:05:15.862'

# get function (finder.find for now)
from gda.factory import Finder
get = Finder.getInstance().find
del Finder

# not executed so types not in: dir(gdaserver)
if False:
	
	# fake imports for fake assignments below
	from gda.data import ObservablePathConstructor
	from gda.data.metadata import GdaMetadata
	from gda.data.metadata import NXMetaDataProvider
	from gda.device.detector import DummyMandelbrotMappingDetector
	from gda.device.detector import NXDetector
	from gda.device.motor import DummyMotor
	from gda.device.scannable import ScannableMotor
	from gda.device.scannable import TwoJawSlitGap
	from gda.device.scannable import TwoJawSlitPosition
	from gda.device.scannable.scannablegroup import ScannableGroup
	from gda.jython import JythonServer
	from gda.util.findableHashtable import FindableHashtable
	from uk.ac.diamond.scisoft.analysis.plotserver import PlotServerBase
	
	# fake assignments for PyDev type-inference
	command_server = JythonServer()
	dummyMandelbrotMappingDetector1D = DummyMandelbrotMappingDetector()
	dummyMandelbrotMappingDetector2D = DummyMandelbrotMappingDetector()
	dummyNXDetector = NXDetector()
	frontjack = ScannableMotor()
	GDAHashtable = FindableHashtable()
	GDAMetadata = GdaMetadata()
	jack = ScannableGroup()
	LeftFrontJack_Motor = DummyMotor()
	leftjack = ScannableMotor()
	mapping_stage_xy = ScannableGroup()
	metashop = NXMetaDataProvider()
	plot_server = PlotServerBase()
	RightFrontJack_Motor = DummyMotor()
	s1 = ScannableGroup()
	s1x1 = ScannableMotor()
	S1X1_motor = DummyMotor()
	s1x2 = ScannableMotor()
	S1X2_motor = DummyMotor()
	s1xcentre = TwoJawSlitPosition()
	s1xsize = TwoJawSlitGap()
	stage_x = ScannableMotor()
	stage_x_motor = DummyMotor()
	stage_y = ScannableMotor()
	stage_y_motor = DummyMotor()
	stage_z_motor = DummyMotor()
	terminallog_path_provider = ObservablePathConstructor()

# real assignments of module-level attributes
command_server = get("command_server")
dummyMandelbrotMappingDetector1D = get("dummyMandelbrotMappingDetector1D")
dummyMandelbrotMappingDetector2D = get("dummyMandelbrotMappingDetector2D")
dummyNXDetector = get("dummyNXDetector")
frontjack = get("frontjack")
GDAHashtable = get("GDAHashtable")
GDAMetadata = get("GDAMetadata")
jack = get("jack")
LeftFrontJack_Motor = get("LeftFrontJack_Motor")
leftjack = get("leftjack")
mapping_stage_xy = get("mapping_stage_xy")
metashop = get("metashop")
plot_server = get("plot_server")
RightFrontJack_Motor = get("RightFrontJack_Motor")
s1 = get("s1")
s1x1 = get("s1x1")
S1X1_motor = get("S1X1_motor")
s1x2 = get("s1x2")
S1X2_motor = get("S1X2_motor")
s1xcentre = get("s1xcentre")
s1xsize = get("s1xsize")
stage_x = get("stage_x")
stage_x_motor = get("stage_x_motor")
stage_y = get("stage_y")
stage_y_motor = get("stage_y_motor")
stage_z_motor = get("stage_z_motor")
terminallog_path_provider = get("terminallog_path_provider")
# so you can import identifiers instead of strings

# don't leak get function
del get
