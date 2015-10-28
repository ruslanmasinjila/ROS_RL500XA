#! /usr/bin/env python

##### IMPORTS ########## 

from __future__ import division
from numpy import *
from math import *
from random import *
from matplotlib.pyplot import *

#############################

def normalizeAngle(originalAngle):

#	Normalizes angle to [-pi,pi]
#
#	INPUT:
#	originalAngle TODO Scalar
#
#	OUTPUT:
#	normalizedAngle [scalar] TODO Scalar

	normalizedAngle=originalAngle%(2*pi)

	if( normalizedAngle>=pi and normalizedAngle<=2*pi ):
    		normalizedAngle=-((2*pi)-normalizedAngle)

	return normalizedAngle

#############################

def estimateOdometryPose(b,previousPose,ut):

#	Estimates the next position and orientation of a 
#	2 wheeled robot using information that comes from the encoders


#	INPUT:
#	distance between the wheels, b TODO Scalar
#	previous position and orientation: TODO 1x3 Matrix
#	control input ut where: TODO 1x2 Matrix
#		ut=[DL DR]
#
#	OUTPUT:
#	current position and orientation TODO [1x3 Matrix]

	
	previousX=previousPose[0,0]
	previousY=previousPose[0,1]
	previousTheta=previousPose[0,2]

	# ut=[DL DR]
	DL=ut[0,0]
	DR=ut[0,1]

	# Calculate the new x coordinate
	currentX	=	previousX + ((DR+DL)/2)*cos(previousTheta + ((DR-DL)/(2*b)));

	# Calculate the new y coordinate
	currentY	=  	previousY +  ((DR+DL)/2)*sin(previousTheta+ ((DR-DL)/(2*b)));

	# Calculate the new Theta
	currentTheta	=	previousTheta+(DR-DL)/b;


	#TODO
	# Normalize results between [-pi,pi]
	currentTheta=normalizeAngle(currentTheta);


	# Put them together
	currentPose=matrix([currentX,currentY,currentTheta]);


	return currentPose

################################


def estimateRelativePose(robotPose,landmarkPose,S):

#Estimates the relative position and orientation of a robot relative to a landmark
#
#   INPUT:
#   Robot Pose (mu=[x y theta]) TODO 1x3 Matrix
#   Landmark Position (landmarkPose=[x y]) TODO 1x3 Matrix
#   Sensor covariances (S=[sigma_rho sigma_phi]) TODO 1x2 Matrix
#                       sigma_rho~Distance error
#                       sigma_phi~Angle error

#   OUTPUT
#   When S=[0 0]:   Estimated relative Pose (Z_bar) TODO 2x1 Matrix
#   Otherwise:      Simulated, actual, noisy Pose (Z) TODO 2x1 Matrix

#   When S=[0 0]:   Estimates the distance and angle of landmark w.r.t robot (Z_bar)
#   Otherwise:      Simulates the actual, noisy distance and angle of landmarkPose w.r.t robot (Z)


	sigma_rho=S[0,0]
	sigma_phi=S[0,1]

	dx=landmarkPose[0,0]-robotPose[0,0]
	dy=landmarkPose[0,1]-robotPose[0,1]
	rho=sqrt(pow(dx,2)+pow(dy,2))

	phi=atan2(dy,dx)

	rho=rho+sigma_rho*gauss(0,1)


	#   Add noise to the measured angle
	#   Find difference between measured noisy angle and robot angle (theta)
	phi=(phi-robotPose[0,2])+sigma_phi*gauss(0,1)

	#   Normalize the results between [-pi,pi]
	phi=normalizeAngle(phi)

	#TODO 1x2 Matrix
	Z=matrix([[rho],[phi]])
	return Z

#############################

def evaluatePredictionJacobians(b,previousPose,ut):


#   Computes the Jacobians G_mut and G_ut
#   G_mut:  Partial derivative of the current pose w.r.t previous pose
#   G_ut:   Partial derivetive of the current pose w.r.t control input

#   INPUT:  
#   Previous Pose of the Robot (previousPose) TODO 1x3 Matrix
#   Control Input (ut) TODO 1x2 Matrix

#   OUTPUT:
#   G_mut TODO 3x3 Matrix
#   G_ut TODO 3x2 Matrix

	# Initialize Jacobians as empty lists
	# Afterwards convert them into Matrices using numpy
        G_mut=[]
        G_ut=[]

        DL=ut[0,0]
        DR=ut[0,1]

        previousTheta=previousPose[0,2]

        G_mut.append([ 1, 0, -((DR+DL)/2)*sin(previousTheta + (DR - DL)/(2*b))])
        G_mut.append([ 0, 1,  ((DR+DL)/2)*cos(previousTheta + (DR - DL)/(2*b))])
        G_mut.append([0, 0,1])

	# Convert G_mut from a list to a matrix using numpy
	G_mut=matrix(G_mut)


        DS=DL+DR;
        DT=((DR-DL)/(2*b))+previousTheta

        G_ut.append([DS*sin(DT)+2*b*cos(DT), -DS*sin(DT)+2*b*cos(DT)])
        G_ut.append([-DS*cos(DT)+2*b*sin(DT), DS*cos(DT)+2*b*sin(DT)])
        G_ut.append([-4,4])

	#Convert G_ut from a list to a matrix using numpy
	G_ut=matrix(G_ut)
        G_ut=(1/(4*b))*G_ut;

	#Put them together
        predictionJacobians=[G_mut,G_ut]

        return predictionJacobians

##########################

def evaluateMeasurementJacobians( currentPose, landmarkPose):

#   Computes the Jacobians Hr and Hl
#   Hr:     Partial derivative of the Estimated Relative Pose w.r.t current pose
#   Hl:     Partial derivetive of the Estimated Relative Pose w.r.t
#           landmark pose


#   INPUT:  
#   Current Pose of the Robot (currentPose) TODO 1x3 Matrix
#   Landmark Pose (landmarjPose) TODO 1x3 Matrix

#   OUTPUT:
#   Hr TODO 2x1 Matrix 
#   Hl TODO 2x1 Matrix


   	# Initialize Jacobians as empty lists
	# Afterwards convert them into matrices using numpy
	Hr=[]
	Hl=[]

    	lx=landmarkPose[0,0]
    	ly=landmarkPose[0,1]
    
    	rx=currentPose[0,0]
   	ry=currentPose[0,1]
    
    	q=sqrt(pow((lx-rx),2)+pow((ly-ry),2))

    	Hr.append([-(lx-rx),-(ly-ry),0])
    	Hr.append([(ly-ry)/q,-(lx-rx)/q,-q])

	#Convert Hr to a matrix using numpy
	Hr=matrix(Hr)
	Hr=(1/q)*Hr
    
    	Hl.append([lx-rx,ly-ry,0])
    	Hl.append([-(ly-ry)/q,(lx-rx)/q,0])

	#Convert Hl to a matrix using numpy
	Hl=matrix(Hl)
	Hl=(1/q)*Hl
	

    	# put the Jacobians together
    	measurementJacobians=[Hr,Hl]

    	return measurementJacobians


########################

def evaluateRelativePoseDifference(Z,Z_bar):

#   Calculates the difference between Estimated (Z_bar) and measured (Z)
#   poses followed by normalization of the results

#   INPUT:TODO 2x1 Matrix
#   Measured noisy relative position of a landmark with respect to robot (Z)
#   Estimated relative postion of a landmark with respect to a robot (Z_bar)
#
#   OUTPUT: TODO 2x1 Matirx
#   Normalized Difference between Z and Z_bar

	Z_diff=Z-Z_bar

	#   Normalize the difference to [-pi,pi]
	Z_diff[1,0]=normalizeAngle(Z_diff[1,0])

	return Z_diff


########################

def getOdometryCovariance(ut,K):

#   Returns the covariance matrix of the wheel odometers

#   INPUT:
#   Control Input (ut=[DL DR]) TODO 1x2 Matrix
#                DL~Left wheel displacement
#                DR~Right wheel displacement

#   Odometry Error Constants (K=[KL KR])
#                KL~Left wheel error
#                KR~Right wheel error
#
#   OUTPUT:
#   Odometer Covariance Matrix: Rt TODO 2x2 Matrix

	KL=K[0,0]
	KR=K[0,1]

	DL=ut[0,0]
	DR=ut[0,1]

	Rt=matrix([[pow((KL*DL),2),0],[0,pow((KR*DR),2)]])
	
	return Rt


########################

def getSensorCovariance(S):

#   Returns the covariance matrix of the Distance Sensor

#   INPUT:
#   Sensor Error Constants (S=[sigma_rho sigma_phi])
#                sigma_rho~Distance error
#                sigma_phi~Angle error
#
#   OUTPUT:
#   Sensor Covariance Matrix: Qt TODO 2x2 Matrix


	sigma_rho=S[0,0]
	sigma_phi=S[0,1]

	Qt=matrix([[pow((sigma_rho),2),0],[0,pow((sigma_phi),2)]])

	return Qt



def selectRandomRobot():

#   Chooses randomly which robot to move

	movingRobot=randint(0,1)

	if(movingRobot==0):
	    stationaryRobot=1
	else:
	    stationaryRobot=0

	moving_stationary=[movingRobot,stationaryRobot]

	return moving_stationary

#########################

def makePlots(mu_expected,mu,robot_id,colors,step_number):

#	Prints the actual vs Filtered Poses

	if(step_number==0):
		ion()
		show()

	mu_expectedX=[]
	mu_expectedY=[]
	mu_expectedTheta=[]

	muX=[]
	muY=[]
	muTheta=[]

	for i in range(len(mu)):

		mu_expectedX.append(mu_expected[i][0,0])
		mu_expectedY.append(mu_expected[i][0,1])

		muX.append(mu[i][0,0])
		muY.append(mu[i][0,1])
	plot(mu_expectedX,mu_expectedY,colors[0])
	plot(muX,muY,colors[1])
	#arrow(mu[-1],mu[-1],cos(mu[-1][0,2]),sin(mu[-1][0,2]),head_width=0.1, head_length=0.2)
	draw()
	
	#	Display graphs for both robots on the same axes	

	#if(robot_id==1):
	#	show(block=False)

def closePlots():
	close("all")



