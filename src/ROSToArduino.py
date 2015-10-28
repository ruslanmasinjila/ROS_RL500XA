#! /usr/bin/env python
#File name ROSToArduino.py

#PUBLICATIONS:
        #Topic name: rosToArduino_tpc   
        #Message type: ros_rl500xa/toArduino_msg
    
#SUBSCRIPTIONS
        #Topic name: joy
        #Message type: sensor_msgs/Joy

##################IMPORTS#########################
from __future__ import division
import rospy
import roslib; roslib.load_manifest('cmvision')
import sys
import cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import *
from ros_rl500xa.msg import *
from sensor_msgs.msg import *
from cmvision.msg import *
from point_cloud2 import *
from ekf2w import *
from math import *
from numpy import *
###################VARIABLES######################

#TODO:
#	1. Invert the x coordinates from Kinect (i.e Multiple the coordinates for x-axis by (-1))
#	2. If pointcloud is NaN. Do not publish or print

class ROSToArduino():
	
	#Constructor
	def __init__(self):

		#Subscribe to "blobs" from cmvision which publishes messages of type "Blobs.msg"
		#self.blobs_sub=rospy.Subscriber("/blobs",Blobs,self.blobs_cb)

		#Subscribe to "joy" topic which publishes messages of type "Joy.msg"
		self.joystickCommands_sub=rospy.Subscriber("joy",Joy,self.joystickCommands_cb)
	
		#Publish "toArduino_msg" messages in "ROSToArduino_tpc" topic
		self.ROSToArduino_pub=rospy.Publisher("ROSToArduino_tpc",toArduino_msg)

		#Subscribe to Visual Trackers (Kinect 1..n where n is the number of kinects)
		self.KinectToROS_sub=rospy.Subscriber("kinectToROS_tpc0",fromObserver_msg,self.observation_cb0)
		self.KinectToROS_sub=rospy.Subscriber("kinectToROS_tpc1",fromObserver_msg,self.observation_cb1)

		# Subscribe to Arduino in order to receive encoder information
		self.ArduinoToROS_sub=rospy.Subscriber("arduinoToROS_tpc0",fromArduino_msg,self.fromArduino_cb0)
		self.ArduinoToROS_sub=rospy.Subscriber("arduinoToROS_tpc1",fromArduino_msg,self.fromArduino_cb1)

		# Initialize parameter Server
		rospy.set_param('visual_tracker','')

		#CV Bridge
		#Create CV Bridge Object
		self.bridge=CvBridge()

		#Initialize CV image
		self.cv_image=None

		#x coordinate of the largest blob
		self.blobX=None

		#y coordinate of the largest blob
		self.blobY=None

		#Image dimensions
		self.image_width=640
		self.image_height=480
	
		#Initialize cloud points
		self.cloud=None
		
		#Subscribe to the raw data coming from registered depth image from Kinect
		#self.image_sub=rospy.Subscriber("/camera/depth_registered/points",PointCloud2, self.kinect_cb)


		#Joystick Properties 
		#LEFT-RIGHT AXIS (axes[0])
		self.LEFT_MIN=0.1
		self.LEFT_MAX=1.2
		self.RIGHT_MIN=-0.1
		self.RIGHT_MAX=-1.2

		#FORWARD-REVERSE AXIS (axes[4])
		self.FORWARD_MIN=0.1
		self.FORWARD_MAX=1.2
		self.REVERSE_MIN=-0.1
		self.REVERSE_MAX=-1.2

		#TURRET ROTATION (axes[3])
		self.CENTER=0.0
		self.C_MAX=-1.1
		self.CC_MAX=1.1
		self.previous_turrent_PWM=1500

		#Wheel Motor PWM values
		#Maximum value is 254. adjust these values for
		#faster/slower movements
		self.PWM_MAX=45
		self.PWM_MIN=40
		rospy.set_param('PWM_MAX',self.PWM_MAX)
		rospy.set_param('PWM_MIN',self.PWM_MIN)
		self.speedToggle=1
		# Set the slowest velocity to non-zer
		# to reduce interference from motors to encoders
		self.PWM_MIN=30

		#Camera Properties
		#Boundaries of the blob (blob should be maintained within BLOB_MIN and BLOB_MAX)
		self.BLOB_MIN=240
		self.BLOB_MAX=400

		#Turret Servo Pulse Widths
		self.PULSE_WIDTH_CC_MAX=1200
		self.PULSE_WIDTH_CENTER=1500
		self.PULSE_WIDTH_C_MAX=1800

		# ROBOT AND LOCALIZATION 
		self.ekf2w=None
		self.movingRobot=None
		self.stationaryRobot=None
		self.display_toggle=1		# Displays/closes graphs
		self.ut=[0,0]
		self.Zt=[0,0]

		# Transformation variables
		self.Tx=0.0				# Kinect's distance from the center of the wheels.
		self.Ty=0.0
		self.radiusLandmark=0.035
		wheelRadius=0.13			# Radius of the wheel in meters
		self.circumference=2*pi*wheelRadius
		self.numStripes=40				# Number of black and white stripes on wheel encoder

	#Callback for handling control commands
	def joystickCommands_cb(self,joystickCmd):

		#Create a message to send to Arduino
		messageToArduino=toArduino_msg()
		
		#Get the Joystick Values
		lr_joystickValue=joystickCmd.axes[0]			# Command for steering the platform left and right
		fr_joystickValue=joystickCmd.axes[4]			# Command for moving the platform forward and reverse
		turret_joystickValue=joystickCmd.axes[3]		# Command for rotating the turret which holds kinect and other sensors
		localization_start=joystickCmd.buttons[7]		# Command which creates and initializes robots with ther initial positions
		localize=joystickCmd.buttons[0]				# Command which executes the main localization function using estimated and measured data
		close_graphs=joystickCmd.buttons[6]			# Command to display Graphs
		getData=joystickCmd.buttons[1]				# Command that requests data from Kinect and Arduino
		

		#Robot States:
		#0=Observing
		#1=Moving
		robot0_state=joystickCmd.buttons[4]
    		robot1_state=joystickCmd.buttons[5]
		speedToggle=joystickCmd.buttons[3]


		#map jostick values to PWM values
		self.mapJoystick(lr_joystickValue,fr_joystickValue,turret_joystickValue,messageToArduino)



		#########################################################################################

		#	Initialize robots if Localization command is received
		if(localization_start==1):
			#	Initialize positions of the robots
			#	Robot0 is always starts at  (x,y,z)=(0,0,0)
			#	Robot1 and the rest start at (x,y,z)=(Distance_from_kinect,0,0)
			self.ekf2w=None
			#initialPoses=[[0,0,0],[0,0.8,0]]
			initialPoses=[[0.305,1.83,pi/2],[0,0,pi/2]]
			self.ekf2w=EKF2W(2,initialPoses)

			#	Close graphs if open and reset the display toggle flag
			self.ekf2w.close_graphs()
			messageToArduino.resetEncoders=1
			print "*************************** LOCALIZATION STARTED *****************************"


		#########################################################################################
		if(getData==1):

			#	Ask Arduino to send Encoder Data
			messageToArduino.sendEncoderData=1
	
			#	Ask Kinect to send its data
			if(self.movingRobot==0):
				rospy.set_param('visual_tracker','/VisualTracker0')

			if(self.movingRobot==1):
				rospy.set_param('visual_tracker','/VisualTracker1')

			#	If Speed is updated, get the latest speed
			self.PWM_MAX=rospy.get_param('PWM_MAX')
			self.PWM_MIN=rospy.get_param('PWM_MIN')
				
		########################################################################################

		# 	Execute Main localization function
		if(localize==1):

			if (self.ut!=[0,0]):
				self.ekf2w.ekf2w_localization(self.movingRobot,self.stationaryRobot,self.ut,self.Zt)
				messageToArduino.resetEncoders=1
				self.movingRobot=None
				self.stationaryRobot=None
				self.ut=[0,0]
				self.Zt=[0,0]


		#########################################################################################
		#Select the robot
		#Select Robot0
		if(robot0_state==1 and robot1_state==0):
			messageToArduino.movingRobot=101
			self.movingRobot=0
			self.stationaryRobot=1

		#Select Robot1
		if(robot0_state==0 and robot1_state==1):
			messageToArduino.movingRobot=102
			self.movingRobot=1
			self.stationaryRobot=0


		# None of the robots is selected
		if(robot0_state==0 and robot1_state==0):
			self.movingRobot=0
			self.stationaryRobot=0

		#Select both Robots
		if(robot0_state==1 and robot1_state==1):
			messageToArduino.movingRobot=999
		#########################################################################################
		#	Close Graphs
		if(close_graphs==1):
			self.ekf2w.close_graphs()

		########################################################################################
		if(speedToggle==1):
			self.speedToggle=self.speedToggle*-1
			
			if(self.speedToggle==1):
				self.PWM_MAX=250
			else:
				self.PWM_MAX=45
		
		########################################################################################

		#Send the message to Arduino
		self.sendToArduino(messageToArduino)



	##############################################################################

	#Callback that processes observation values obtained by stationary Robot
	def observation_cb0(self,messageFromKinect):

		# Set the Tx for Robot 0
		self.Tx=0.27
		self.Ty=0
		self.getZt(messageFromKinect)

	
	def observation_cb1(self,messageFromKinect):

		# Set the Tx for Robot 1
		self.Tx=0.57
		self.Ty=0
		self.getZt(messageFromKinect)
	def getZt(self,messageFromKinect):

		print "Kinect Data From:",messageFromKinect.observerID
		
		if (messageFromKinect.observerID=="/VisualTracker0"):

			x=messageFromKinect.coordinates[2]*(-1)
			x=x-self.Tx-self.radiusLandmark
			y=self.Ty+messageFromKinect.coordinates[0]

		else:
			x=messageFromKinect.coordinates[2]
			x=x+self.Tx+self.radiusLandmark
			y=self.Ty+messageFromKinect.coordinates[0]*(-1)

		print x,y



		# Find rho
		rho=sqrt(x**2+y**2)
		theta=atan2(y,x)

		print "Rho:",rho
		print "Theta:",theta*(180/pi)

		self.Zt=[rho,theta]


	##############################################################################	

	#	TODO: Convert DL and DR to meters using radius/diameter of the wheels
	def fromArduino_cb0(self,messageFromArduino):
		self.getUt(messageFromArduino)

	def fromArduino_cb1(self,messageFromArduino):
		self.getUt(messageFromArduino)

	def getUt(self,messageFromArduino):
		print "Encoder ticks from",messageFromArduino.robotID,":",messageFromArduino.DL,messageFromArduino.DR
		self.ut=[(messageFromArduino.DL*self.circumference)/self.numStripes,(messageFromArduino.DR*self.circumference)/self.numStripes]


	###############################################################################

	
	#Maps joystick values to corresponding PWM value and direction
	def mapJoystick(self,lr_joystickValue,fr_joystickValue,turret_joystickValue,messageToArduino):

	#Determine Direction of the robot (Left,Right,Forward,Reverse)

		#if turning left
		if(lr_joystickValue>self.LEFT_MIN and lr_joystickValue<self.LEFT_MAX):
			messageToArduino.xAxisDirection="l"
			messageToArduino.lr_pwm=(((lr_joystickValue-self.LEFT_MIN)*(self.PWM_MAX-self.PWM_MIN))/
						(self.LEFT_MAX-self.LEFT_MIN)+self.PWM_MIN)

		#if turning right
		if (lr_joystickValue>self.RIGHT_MAX and lr_joystickValue<self.RIGHT_MIN):
			messageToArduino.xAxisDirection="r"
			messageToArduino.lr_pwm=(((lr_joystickValue-self.RIGHT_MIN)*(self.PWM_MAX-self.PWM_MIN))/
						(self.RIGHT_MAX-self.RIGHT_MIN)+self.PWM_MIN)

		#if moving forward
		if (fr_joystickValue>self.FORWARD_MIN and fr_joystickValue<self.FORWARD_MAX):
			messageToArduino.yAxisDirection="f"
			messageToArduino.fr_pwm=(((fr_joystickValue-self.FORWARD_MIN)*(self.PWM_MAX-self.PWM_MIN))/
						(self.FORWARD_MAX-self.FORWARD_MIN)+self.PWM_MIN)


		#if moving back
		if (fr_joystickValue>self.REVERSE_MAX and fr_joystickValue<self.REVERSE_MIN):
			messageToArduino.yAxisDirection="b"
			messageToArduino.fr_pwm=(((fr_joystickValue-self.REVERSE_MIN)*(self.PWM_MAX-self.PWM_MIN))/
						(self.REVERSE_MAX-self.REVERSE_MIN)+self.PWM_MIN)


	#Determine Direction of rotation of the turret (Clockwise (C) or Counter clockwise (CC))

		#If rotating in Counter clockwise direction
		if(turret_joystickValue>self.CENTER):

			if(turret_joystickValue>self.CC_MAX):
				turret_joystickValue=self.CC_MAX

			messageToArduino.turret_pulse_width=\
					(((turret_joystickValue-self.CENTER)*(self.PULSE_WIDTH_CC_MAX-self.PULSE_WIDTH_CENTER))/
					(self.CC_MAX-self.CENTER)+self.PULSE_WIDTH_CENTER)


		#If rotating in Clockwise direction
		if(turret_joystickValue<self.CENTER):

			if(turret_joystickValue<self.C_MAX):
				turret_joystickValue=self.C_MAX

			messageToArduino.turret_pulse_width=\
					(((turret_joystickValue-self.CENTER)*(self.PULSE_WIDTH_C_MAX-self.PULSE_WIDTH_CENTER))/
					(self.C_MAX-self.CENTER)+self.PULSE_WIDTH_CENTER)


            	#If Joystick is in the middle
		if(turret_joystickValue==self.CENTER):
			messageToArduino.turret_pulse_width=self.PULSE_WIDTH_CENTER
	

		#Save turrent_PWM values
		self.previous_turrent_PWM=messageToArduino.turret_pulse_width

	def sendToArduino(self,messageToArduino):

		#Publish the Message
		self.ROSToArduino_pub.publish(messageToArduino)

def main():

	#Initialize node
	rospy.init_node("ROSToArduino")
	print "ROSToArduino Initialized..."

	#Create object
	ROSToArduino_node=ROSToArduino()

	#Continuous Loop
	rospy.spin()

if __name__ == "__main__":
    main()
