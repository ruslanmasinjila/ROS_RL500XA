from __future__ import division
from numpy import *
from math import *
from random import *
from ekf_functions import *

'''
b=5.64
ut=[5.2,3.14]
previousPose=[2.38,-15.6,pi/2]
landmarkPose=[-5.8,0.5,3*pi/5]
S=[0.1,0.01]
robotPose=[-6.91,5.33,pi/6]
K=[0.1,1.2]

previousPose=matrix(previousPose)
landmarkPose=matrix(landmarkPose)
ut=matrix(ut)
S=matrix(S)
robotPose=matrix(robotPose)
K=matrix(K)

moving_stationary=selectRandomRobot()
print moving_stationary
'''

lst=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(lst)):
	print i
