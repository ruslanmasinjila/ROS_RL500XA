# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ruslan/ros_workspace/cmvision

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ruslan/ros_workspace/cmvision/build

# Utility rule file for ROSBUILD_genmsg_cpp.

# Include the progress variables for this target.
include CMakeFiles/ROSBUILD_genmsg_cpp.dir/progress.make

CMakeFiles/ROSBUILD_genmsg_cpp: ../msg_gen/cpp/include/cmvision/Blob.h
CMakeFiles/ROSBUILD_genmsg_cpp: ../msg_gen/cpp/include/cmvision/Blobs.h

../msg_gen/cpp/include/cmvision/Blob.h: ../msg/Blob.msg
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/share/roslib/bin/gendeps
../msg_gen/cpp/include/cmvision/Blob.h: ../manifest.xml
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/share/roslang/manifest.xml
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/share/roscpp/manifest.xml
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/stacks/vision_opencv/opencv2/manifest.xml
../msg_gen/cpp/include/cmvision/Blob.h: /opt/ros/fuerte/stacks/vision_opencv/cv_bridge/manifest.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ruslan/ros_workspace/cmvision/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../msg_gen/cpp/include/cmvision/Blob.h"
	/opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py /home/ruslan/ros_workspace/cmvision/msg/Blob.msg

../msg_gen/cpp/include/cmvision/Blobs.h: ../msg/Blobs.msg
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/roslib/bin/gendeps
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/std_msgs/msg/Header.msg
../msg_gen/cpp/include/cmvision/Blobs.h: ../msg/Blob.msg
../msg_gen/cpp/include/cmvision/Blobs.h: ../manifest.xml
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/roslang/manifest.xml
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/roscpp/manifest.xml
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/stacks/vision_opencv/opencv2/manifest.xml
../msg_gen/cpp/include/cmvision/Blobs.h: /opt/ros/fuerte/stacks/vision_opencv/cv_bridge/manifest.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/ruslan/ros_workspace/cmvision/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../msg_gen/cpp/include/cmvision/Blobs.h"
	/opt/ros/fuerte/share/roscpp/rosbuild/scripts/genmsg_cpp.py /home/ruslan/ros_workspace/cmvision/msg/Blobs.msg

ROSBUILD_genmsg_cpp: CMakeFiles/ROSBUILD_genmsg_cpp
ROSBUILD_genmsg_cpp: ../msg_gen/cpp/include/cmvision/Blob.h
ROSBUILD_genmsg_cpp: ../msg_gen/cpp/include/cmvision/Blobs.h
ROSBUILD_genmsg_cpp: CMakeFiles/ROSBUILD_genmsg_cpp.dir/build.make
.PHONY : ROSBUILD_genmsg_cpp

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_genmsg_cpp.dir/build: ROSBUILD_genmsg_cpp
.PHONY : CMakeFiles/ROSBUILD_genmsg_cpp.dir/build

CMakeFiles/ROSBUILD_genmsg_cpp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_genmsg_cpp.dir/clean

CMakeFiles/ROSBUILD_genmsg_cpp.dir/depend:
	cd /home/ruslan/ros_workspace/cmvision/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ruslan/ros_workspace/cmvision /home/ruslan/ros_workspace/cmvision /home/ruslan/ros_workspace/cmvision/build /home/ruslan/ros_workspace/cmvision/build /home/ruslan/ros_workspace/cmvision/build/CMakeFiles/ROSBUILD_genmsg_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_genmsg_cpp.dir/depend

