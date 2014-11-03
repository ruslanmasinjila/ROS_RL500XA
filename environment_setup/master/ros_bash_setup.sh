#!/bin/bash
NAME="##### MASTER #####"
if grep -q "$NAME" ~/.bashrc; then
  echo "Environment Already Set"
else
  echo "">>~/.bashrc
  echo "##### MASTER #####">>~/.bashrc
  echo "source ~/.ros_single">>~/.bashrc
  echo "#source ~/.ros_distributed">>~/.bashrc
  cp .ros_single ~/
  cp .ros_distributed ~/
  cp .bash_aliases ~/
  cp .vimrc ~/

  #Robot ID setup
  rm ~/ros_workspace/ros_rl500xa/arduino/rl_500xa/src/robot_variables.txt
  touch ~/ros_workspace/ros_rl500xa/arduino/rl_500xa/src/robot_variables.txt
  echo "//********************************ROBOT VARIABLES*********************************">>~/ros_workspace/ros_rl500xa/arduino/rl_500xa/src/robot_variables.txt
  echo "int robotID=0;">>~/ros_workspace/ros_rl500xa/arduino/rl_500xa/src/robot_variables.txt
  echo "int allRobots=999;">>~/ros_workspace/ros_rl500xa/arduino/rl_500xa/src/robot_variables.txt
  echo "int movingRobot=-1;">>~/ros_workspace/ros_rl500xa/arduino/rl_500xa/src/robot_variables.txt
  echo "Finished setting ROS Environment for MASTER" 
fi
echo "Press Enter to exit"
read


