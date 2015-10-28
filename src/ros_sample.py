#! /usr/bin/env python
import rospy
import roslib
from std_msgs.msg import String

class ros_sample():

	def __init__(self):

		# Declare class variables here
		
		# Print Statement to avoid error
	
		print "ros_sample running..."

		
		self.parameterServer()
		self.writeToFile("This is second line")
		self.writeToFile("This is the third line")
		lst=[1,2,3,4,5]
		self.writeToFile(str(1)+" "+str(lst))

	def parameterServer(self):
		rospy.set_param(rospy.get_name(), "Hello World")

	def writeToFile(self,data):
		with open("robot0.txt","a") as myfile:
			myfile.write(data+'\n')
		

def main():

        #Initialize node
        rospy.init_node("ros_sample")

        #Create object
        rose_sample_node=ros_sample()

        #Continuous Loop
        rospy.spin()

if __name__ == "__main__":
    main()



