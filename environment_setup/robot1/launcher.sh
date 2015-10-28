#!/bin/bash
#source ~/.bashrc

xterm -hold -e "roslaunch ros_rl500xa ros_rl500xa1.launch"&
sleep 2
xterm -hold -e "roslaunch ros_rl500xa kinect1.launch"


