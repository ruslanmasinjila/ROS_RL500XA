FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/ros_rl500xa/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/ros_rl500xa/fromArduino_msg.h"
  "../msg_gen/cpp/include/ros_rl500xa/fromObserver_msg.h"
  "../msg_gen/cpp/include/ros_rl500xa/toArduino_msg.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
