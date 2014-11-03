#Script that concatenates different segments of the 
#Arduino Sketch.
cd src
rm rl_500xa.ino
touch rl_500xa.ino

#Concatenate Header
cat headers.txt>>rl_500xa.ino

#Concatenate Prototypes
cat prototypes.txt>>rl_500xa.ino

#Concatenate variables
cat ROS_variables.txt>>rl_500xa.ino
cat teleop_variables.txt>>rl_500xa.ino
cat encoder_variables.txt>>rl_500xa.ino
cat turret_variables.txt>>rl_500xa.ino
cat robot_variables.txt>>rl_500xa.ino
#>>Add more here

#Concatenate setup
cat setup.txt>>rl_500xa.ino

#Concatenate loop
cat loop.txt>>rl_500xa.ino

#Concatenate Functions
cat ROS_functions.txt>>rl_500xa.ino
cat teleop_functions.txt>>rl_500xa.ino
cat encoder_functions.txt>>rl_500xa.ino
cat turret_functions.txt>>rl_500xa.ino
##>>Add more here
echo "Concatenation Complete"

