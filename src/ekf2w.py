#! /usr/bin/env python

########## IMPORTS ##########
from __future__ import division
from math import *
from numpy import *
from robot import *
from random import *
from ekf_functions import *
#############################


class EKF2W:


	# Creates and Initializes robots with initial positions
	# initialPoses=[[x0,y0,theta0],[x0,y0,theta0],...[xn,yn,thetaN]]
	def __init__(self,numRobots,initialPoses):


	#List of Robots
		self.Robots=[]

	#Number of Steps
		self.stepNumber=0

	# Create Robots
		for robotID in range(numRobots):
			self.Robots.append(Robot(robotID,initialPoses[robotID]))


	

	############################################################

	# Main Localization Function
	def ekf2w_localization(self,movingRobot,stationaryRobot,ut,Z):
		

		# Convert Ut and Z to numpy matrices
		ut=matrix(ut)

		#
		Z=matrix([[Z[0]],[Z[1]]])
		#############################################
		if(Z[1,0]>=(178*pi/180) or Z[1,0]<=(-178*pi/180)):
			Z[1,0]=pi
		
		elif(Z[1,0]>=(-2*pi/180) and Z[1,0]<=(2*pi/180)):
			Z[1,0]=0
		else:
			None
		############################################

		
		# Set the current Step which is the last element in a list
		currentStep=-1

		

		#   Compute the current noiseless pose from previous noiseless Pose
		self.Robots[movingRobot].mu_expected.append(estimateOdometryPose(self.Robots[movingRobot].b,self.Robots[movingRobot].mu_expected[currentStep],ut))
		


		#   Estimate the predicted (priori) state of the robot  from previous filtered pose and control input ut
		mu_bar=estimateOdometryPose(self.Robots[movingRobot].b,self.Robots[movingRobot].mu[currentStep],ut)

		#   Compute the partial derivatives of the predicted state w.r.t control input(G_ut) and w.r.t previous
		#   corrected state (G_mut).
		[G_mut, G_ut]=evaluatePredictionJacobians(self.Robots[movingRobot].b,self.Robots[movingRobot].mu[currentStep],ut)


		#   Estimate Z_bar
		Z_bar=estimateRelativePose(mu_bar,self.Robots[stationaryRobot].mu[currentStep],self.Robots[movingRobot].S0)

		
		#   Estimate Z_diff
		Z_diff=evaluateRelativePoseDifference(Z,Z_bar)

		#############################################################
		#updatedK=abs(Z_diff[1,0]/pi)
		#self.Robots[movingRobot].K=matrix([updatedK,updatedK])
		##############################################################


		#   Determine the covariance Matrix of the wheel encoders
		Rt=getOdometryCovariance(ut,self.Robots[movingRobot].K)


		
		#   Estimate the predicted (priori) Covariance (Sigma Bar)
		sigma_bar=G_mut*self.Robots[movingRobot].sigma[currentStep]*(transpose(G_mut)) + G_ut*Rt*(transpose(G_ut))


		



		#   Estimate the partial derivative of the observation/measurement w.r.t to
		#   predicted state (priori)
		[Hr,Hl]=evaluateMeasurementJacobians(mu_bar,self.Robots[stationaryRobot].mu[currentStep])
		#######################################
		#Hl=Hl*0
		#######################################


		
		#   Determine the covariance matrix of the sensors
		Qt=getSensorCovariance(self.Robots[movingRobot].S)


		
		#   Calculate innovation (residula) covariance
		S= (Hr)*(sigma_bar)*(transpose(Hr))+(Hl)*(self.Robots[stationaryRobot].sigma[currentStep])*(transpose(Hl))+Qt

		
		#   Calculate Kalman Gain (Kgain)
		Kgain=  (sigma_bar)*(transpose(Hr))*(linalg.inv(S))

		#   Update mean
		self.Robots[movingRobot].mu.append(mu_bar+(transpose(Kgain*Z_diff)))

		#   Normalize theta to [-pi,pi]
		self.Robots[movingRobot].mu[currentStep][0,2]=normalizeAngle(self.Robots[movingRobot].mu[currentStep][0,2])


		#   Update Covariance
		self.Robots[movingRobot].sigma.append((identity(3)-Kgain*Hr)*sigma_bar)
		print "Robot Number:",movingRobot
		print "Odometers",self.Robots[movingRobot].mu_expected[-1][0,0],self.Robots[movingRobot].mu_expected[-1][0,1],self.Robots[movingRobot].mu_expected[-1][0,2]*(180/pi)
		print "Filtered:", self.Robots[movingRobot].mu[-1][0,0],self.Robots[movingRobot].mu[-1][0,1],self.Robots[movingRobot].mu[-1][0,2]*(180/pi)


		#	Draw the new position on graph

		if(movingRobot==0):
			colors=["bx-","rx-"]
		else:
			colors=["cx-","rx-"]
		makePlots(self.Robots[movingRobot].mu_expected[-2:],\
		self.Robots[movingRobot].mu[-2:],\
		self.Robots[movingRobot].robot_id,\
		colors,\
		self.stepNumber)

		# Write to external File
		self.writeToFile(self.stepNumber,movingRobot)


		#  Print and Increment the number of localization steps
		print "Step Number:",self.stepNumber
		self.stepNumber=self.stepNumber+1




	def display_graphs(self):
		
		#	Plot the graph for the first robot		
		colors=["gx-","bx-","rx-"]
		makePlots(self.Robots[0].mu_expected,self.Robots[0].mu,self.Robots[0].robot_id,colors)

		
		#	Plot the graph for the second robot
		colors=["cx-","yx-","yx-"]
		makePlots(self.Robots[1].mu_expected,self.Robots[1].mu,self.Robots[1].robot_id,colors)


	def close_graphs(self):
		closePlots()

	

	#	Writes ekf and odometry data to external files.
        def writeToFile(self,stepNumber,movingRobot):

                xEncoder=str(self.Robots[movingRobot].mu_expected[-1][0,0])
                yEncoder=str(self.Robots[movingRobot].mu_expected[-1][0,1])
                thetaEncoder=str(self.Robots[movingRobot].mu_expected[-1][0,2])

                xEKF=str(self.Robots[movingRobot].mu[-1][0,0])
                yEKF=str(self.Robots[movingRobot].mu[-1][0,1])
                thetaEKF=str(self.Robots[movingRobot].mu[-1][0,2])

                c00=str(self.Robots[movingRobot].sigma[-1][0,0])
                c01=str(self.Robots[movingRobot].sigma[-1][0,1])
                c02=str(self.Robots[movingRobot].sigma[-1][0,2])
                c10=str(self.Robots[movingRobot].sigma[-1][1,0])
                c11=str(self.Robots[movingRobot].sigma[-1][1,1])
                c12=str(self.Robots[movingRobot].sigma[-1][1,2])
                c20=str(self.Robots[movingRobot].sigma[-1][2,0])
                c21=str(self.Robots[movingRobot].sigma[-1][2,1])
                c22=str(self.Robots[movingRobot].sigma[-1][2,2])

                encoder_data=str(stepNumber)+" "+str(movingRobot)+" "+xEncoder+" "+yEncoder+" "+thetaEncoder+'\n'
                ekf_data=str(stepNumber)+" "+str(movingRobot)+" "+xEKF+" "+yEKF+" "+thetaEKF+" "+c00+" "+c01+" "+c02+" "+c10+" "+c11+" "+c12+" "+c20+" "+c21+" "+c22+'\n'

                with open("encoder_data.txt","a") as encoderFile:
			if(stepNumber!=0):
				encoderFile.write(encoder_data)
			else:
				encoderFile.write("==============================================================================\n")    
				encoderFile.write(encoder_data)

                with open("ekf_data.txt","a") as ekfFile:
			if(stepNumber!=0):
				ekfFile.write(ekf_data)  
			else:
				ekfFile.write("==============================================================================\n")    
				ekfFile.write(ekf_data)  

 
