alias launch='roslaunch ros_rl500xa ros_rl500xa.launch'
alias rosvc='~/ros_workspace/ros_rl500xa/scripts/versionControl.sh'
alias rosbp='~/ros_workspace/ros_rl500xa/scripts/buildProject.sh'
alias inobp='cd ~/ros_workspace/ros_rl500xa/arduino/rl_500xa/;sh concatenator.sh;ino build;cd ~/ros_workspace/ros_rl500xa/'
alias upload='cd ~/ros_workspace/ros_rl500xa/arduino/rl_500xa/;ino upload;cd ~/ros_workspace/ros_rl500xa/'

alias usbcam='roslaunch usb_cam usb_cam.launch'
alias cmcal='rosrun cmvision colorgui image:=/kinect1/rgb1/image_color& gedit ~/ros_workspace/cmvision/colors.txt'
alias cmvision='roslaunch cmvision cmvision.launch'
alias launcher='~/ros_workspace/ros_rl500xa/environment_setup/robot1/launcher.sh'
