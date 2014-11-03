#! /usr/bin/env python
#File name ROSToArduino.py

#PUBLICATIONS:
        #Topic name: rosToArduino_tpc   
        #Message type: ros_rl500xa/toArduino_msg
    
#SUBSCRIPTIONS
        #Topic name: joy
        #Message type: sensor_msgs/Joy

##################IMPORTS#########################
import rospy
from std_msgs.msg import *
from ros_rl500xa.msg import *
from sensor_msgs.msg import *
###################VARIABLES######################


class ROSToArduino():
	
	#Subsciber to "joy" topic
	joystickCommands_sub=None

	#Publisher of <ROSToArduino_tpc>
	ROSToArduino_pub=None

	

	#Constructor
	def __init__(self):

		#Subscribe to "joy" topic which publishes messages of type "Joy.msg"
		self.joystickCommands_sub=rospy.Subscriber("joy",Joy,self.joystickCommands_cb)
	
		#Publish "toArduino_msg" messages in "ROSToArduino_tpc" topic
		self.ROSToArduino_pub=rospy.Publisher("ROSToArduino_tpc",toArduino_msg)

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

		#PWM values
		#Maximum value is 254. adjust these values for
		#faster/slower movements
		self.PWM_MAX=100
		self.PWM_MIN=0

		#Servo Pulse Widths
		self.PULSE_WIDTH_CC_MAX=1200
		self.PULSE_WIDTH_CENTER=1500
		self.PULSE_WIDTH_C_MAX=1800

	#Callback for handling control commands
	def joystickCommands_cb(self,joystickCmd):

		#Create a message to send to Arduino
		messageToArduino=toArduino_msg()
		
		#Get the Joystick Values
		lr_joystickValue=joystickCmd.axes[0]
		fr_joystickValue=joystickCmd.axes[4]
		turret_joystickValue=joystickCmd.axes[3]

		#Robot States:
		#0=Observing
		#1=Moving
		robot0_state=joystickCmd.buttons[4]
    		robot1_state=joystickCmd.buttons[5]

		#map jostick values to PWM values
		self.map(lr_joystickValue,fr_joystickValue,turret_joystickValue,messageToArduino)

		#Select the robot
		#Select Robot0
		if(robot0_state==1 and robot1_state==0):
			messageToArduino.movingRobot=101

		#Select Robot1
		if(robot0_state==0 and robot1_state==1):
			messageToArduino.movingRobot=102

		#Select both Robots
		if(robot0_state==1 and robot1_state==1):
			messageToArduino.movingRobot=999

		
		#Send the message to Arduino
		self.sendToArduino(messageToArduino)

	
	#Maps joystick values to corresponding PWM value and direction
	def map(self,lr_joystickValue,fr_joystickValue,turret_joystickValue,messageToArduino):

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
	

		#print turret_joystickValue,messageToArduino.turret_pulse_width


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
