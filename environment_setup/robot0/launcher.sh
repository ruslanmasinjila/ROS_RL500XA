#!/bin/bash
#source ~/.bashrc

xterm -hold -e "roslaunch ros_rl500xa ros_rl500xa0.launch"&
sleep 2
xterm -hold -e "roslaunch ros_rl500xa kinect0.launch"


