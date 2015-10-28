#! /usr/bin/env python

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
from numpy import *
from matplotlib.pyplot import *
from time import *

class VisualTracker():
    
        #Constructor
        def __init__(self):

                #Subscribe to the raw data coming from registered depth image from Kinect
                self.depthImage_sub=rospy.Subscriber("/camera/depth_registered/points",PointCloud2, self.kinect_cb)
		self.RGBImage_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.rgbCallback)

		#Publish Distance and Orientation from Kinect to ROSToArduino
                self.KinectToROS_pub=rospy.Publisher("kinectToROS_tpc",fromObserver_msg)

                #Subscribe to "joy" topic which publishes messages of type "Joy.msg"
                self.joystickCommands_sub=rospy.Subscriber("joy",Joy,self.joystickCommands_cb)



                #CV Bridge
                #Create CV Bridge Object
		cv.NamedWindow("Image window", 1)
                self.bridge=CvBridge()

                #Initialize CV image
                self.cv_image=None
                
		#Image dimensions
                self.image_width=640
                self.image_height=480

		self.lineX=320
		self.lineY=240
		self.lineWidth=40
		

                #Initialize cloud self.points
                self.cloud=None


                #Joystick Properties 
                #LEFT-RIGHT AXIS (axes[0])
                self.HORIZONTAL_MAX=-1.2
                self.HORIZONTAL_MIN=1.2
		self.lineX_MIN=self.lineWidth
		self.lineX_MAX=self.image_width-self.lineWidth

                #FORWARD-REVERSE AXIS (axes[4])
                self.VERTICAL_MAX=-1.2
                self.VERTICAL_MIN=1.2
		self.lineY_MIN=self.lineWidth
		self.lineY_MAX=self.image_height-self.lineWidth

		


        #Callback for handling control commands
        def joystickCommands_cb(self,joystickCmd):
                lr_joystickValue=joystickCmd.axes[0]                    # Command for steering the platform left and right
                ud_joystickValue=joystickCmd.axes[1]                    # Command for moving the platform forward and reverse


                #map jostick values to PWM values
                self.mapJoystick(lr_joystickValue,ud_joystickValue)

	def mapJoystick(self, lr_joystickValue,ud_joystickValue):
                #left/right
                self.lineX=int(((lr_joystickValue-self.HORIZONTAL_MIN)*(self.lineX_MAX-self.lineX_MIN))/(self.HORIZONTAL_MAX-self.HORIZONTAL_MIN)+self.lineX_MIN)

                #up/down
                self.lineY=int(((ud_joystickValue-self.VERTICAL_MIN)*(self.lineY_MAX-self.lineY_MIN))/(self.VERTICAL_MAX-self.VERTICAL_MIN)+self.lineY_MIN)




  	def rgbCallback(self,data):
    		try:
      			cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
    		except CvBridgeError, e:
      			print e

		cv.Line(cv_image,(self.lineX-self.lineWidth,self.lineY),(self.lineX+self.lineWidth,self.lineY),(0,255,),3)
    		cv.ShowImage("Image window", cv_image)
    		cv.WaitKey(1)


        #Callback handling Kinect's raw depth images
        def kinect_cb(self,rawDepthImage):

		# If data is requested for localization
		if(rospy.get_param('visual_tracker')==rospy.get_name()):
		
			self.cloud= read_points(rawDepthImage, field_names=None, skip_nans=False, uvs=[])

			# Convert a cloud generator to a list
			self.points = []
			for pt in self.cloud:
				pt = list(pt)
				pt.append(1)
				self.points.append(pt)

			nearestPoint=self.getNearestPoint()
			print nearestPoint[2]


			# Create a new message to be sent to ROSToArduino
			messageToROS=fromObserver_msg()
			messageToROS.observerID=rospy.get_name()
			messageToROS.coordinates=(nearestPoint)
			self.KinectToROS_pub.publish(messageToROS)
			
			# Reset the visual_tracker parameter
			rospy.set_param('visual_tracker','')





		
	
	# Gets the nearest point of the cylinder to Kinect
	def getNearestPoint(self):	

		startIndex=(self.image_width*self.lineY)+(self.lineX-self.lineWidth)

		endIndex=(self.image_width*self.lineY)+(self.lineX+self.lineWidth)

		# Initialize nearest point [large number]
		nearestPoint=[1000,1000,1000]


		for index in range(startIndex,endIndex):
			if(self.points[index][2]<=nearestPoint[2]):
				nearestPoint=self.points[index]

		return nearestPoint


def main():

        #Initialize node
        rospy.init_node("VisualTracker")
        print "VisualTracker Initialized..."

        #Create object
        VisualTracker_node=VisualTracker()

        #Continuous Loop
        rospy.spin()

if __name__ == "__main__":
    main()

