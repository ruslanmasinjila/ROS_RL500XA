FILE(REMOVE_RECURSE
  "../src/ros_rl500xa/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/ros_rl500xa/msg/__init__.py"
  "../src/ros_rl500xa/msg/_toArduino_msg.py"
  "../src/ros_rl500xa/msg/_fromArduino_msg.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
