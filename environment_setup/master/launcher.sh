#!/bin/bash
#source ~/.bashrc

# Launch ROSToArduino.py
#xterm -hold -e "roscore"
xterm -hold -e "roslaunch ros_rl500xa ros_rl500xa.launch"&
sleep 2
xterm -hold -e "roslaunch openni_launch openni.launch depth_registration:=true"&
sleep 2
xterm -hold -e "roslaunch cmvision cmvision.launch node_name:=cmvision blob_name:=/blobs rgb_name:=/camera/rgb"


