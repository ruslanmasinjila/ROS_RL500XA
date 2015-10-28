#! /usr/bin/env python
#File name: robot.py
#Handles robot properties, position, orientations, and covariances

########## IMPORTS ##########
from __future__ import division
import rospy
from numpy import *
from random import *
from math import *
#############################


class Robot:

########## ROBOT PROPERTIES ########## 


########## CONSTRUCTOR ##########

	def __init__(self,robot_id,initialPose):

		#Initialize node
		#rospy.init_node("ROBOT")
		#self.robot_id=rospy.get_name()

		# Set the Robot ID
		self.robot_id=robot_id

		
		#Distance between wheels:
		self.b=0.42


		#Robot Positions
		#The expected pose is the pose of the robot determined using only internal
		#encoders assuming there is no noise. This is the "Perfect Pose"
		self.mu_expected=[]


		#The actual pose is the real pose of the robot (Strictly for simulations only)
		#In practise, this is not known. 
		self.mu_actual=[]

		#Filtered Robot pose. This is the pose that is calculated
		# using the Extended Kalman Filter
		self.mu=[]

		#Covariance matrices. Diagonal elements sigma(1,1),sigma(2,2) and
		#sigma(3,3) are the covariances for x,y and theta respectively
		self.sigma=[]

		#Initial Position of the robot. The leading robot is
		# at [x,y,theta]=[0,0,0] by default
		self.xInit=0
		self.yInit=0
		self.thetaInit=0

		########## SENSOR PROPERTIES ##########

		#Error in Distance Measurements
		self.sigma_rho=0.001

		#Error in Orientation measurements
		self.sigma_phi=0.1

		#S0 is used when estimating the relative position and orientation
		# of a landmark
		#S is used to simulate actual, noisy measurement of the orientation
		self.S0=matrix([0,0])
		self.S=matrix([self.sigma_rho,self.sigma_phi])

		########## CONTROL PROPERTIES ##########

		#Odometry Noise
		self.KL=0.3
		self.KR=0.3
		self.K=matrix([self.KL,self.KR])
		

		#Distances from the encoder.
		#Comes from Arduino through parameter Server
		#For simulation purposes, DL and DR should not be 
		#significantly higher than b, the distance between the wheels.
		self.DL=self.b
		self.DR=self.b

		#Total Distance travelled by each wheel.
		#(For simulations only)
		self.totalDL=0
		self.totalDR=0
		self.distanceCovered=[self.totalDL,self.totalDR]


		########################################
		'''
		# TODO For now use random initialization
		# if not the leading robot, initialize
		# the starting position randomly or
		# use information coming from kinect and
		# digital motors
		if(self.robot_id != 0):
			self.xInit=200+gauss(0,1)
			self.yInit=200+gauss(0,1)
			self.thetaInit=gauss(0,1)
		'''
		#######################################
		self.xInit=initialPose[0]
		self.yInit=initialPose[1]
		self.thetaInit=initialPose[2]
		######################################		
		# If leading robot, set its initial position to origin
		# Set its covariance matrix to all zeroes.
		self.mu_expected.append(matrix([self.xInit,self.yInit,self.thetaInit]))
		self.mu_actual.append(matrix([self.xInit,self.yInit,self.thetaInit]))
		self.mu.append(matrix([self.xInit,self.yInit,self.thetaInit]))

		if(self.robot_id==0):
			print "##########################################"
		print "Robot",self.robot_id,"Initialized..."
		print "Initial Position...",self.mu_actual
		print "##########################################"

		
 		#Continuous loop to prevent the node from exiting
		#rospy.spin()


