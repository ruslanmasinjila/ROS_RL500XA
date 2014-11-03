/* Auto-generated by genmsg_cpp for file /home/ruslan/ros_workspace/ros_rl500xa/msg/fromArduino_msg.msg */
#ifndef ROS_RL500XA_MESSAGE_FROMARDUINO_MSG_H
#define ROS_RL500XA_MESSAGE_FROMARDUINO_MSG_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"


namespace ros_rl500xa
{
template <class ContainerAllocator>
struct fromArduino_msg_ {
  typedef fromArduino_msg_<ContainerAllocator> Type;

  fromArduino_msg_()
  : DL(0.0)
  , DR(0.0)
  {
  }

  fromArduino_msg_(const ContainerAllocator& _alloc)
  : DL(0.0)
  , DR(0.0)
  {
  }

  typedef float _DL_type;
  float DL;

  typedef float _DR_type;
  float DR;


  typedef boost::shared_ptr< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct fromArduino_msg
typedef  ::ros_rl500xa::fromArduino_msg_<std::allocator<void> > fromArduino_msg;

typedef boost::shared_ptr< ::ros_rl500xa::fromArduino_msg> fromArduino_msgPtr;
typedef boost::shared_ptr< ::ros_rl500xa::fromArduino_msg const> fromArduino_msgConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace ros_rl500xa

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> > {
  static const char* value() 
  {
    return "523793fd4bc77900491fb58970438a6d";
  }

  static const char* value(const  ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x523793fd4bc77900ULL;
  static const uint64_t static_value2 = 0x491fb58970438a6dULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> > {
  static const char* value() 
  {
    return "ros_rl500xa/fromArduino_msg";
  }

  static const char* value(const  ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float32 DL\n\
float32 DR\n\
\n\
";
  }

  static const char* value(const  ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.DL);
    stream.next(m.DR);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct fromArduino_msg_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::ros_rl500xa::fromArduino_msg_<ContainerAllocator> & v) 
  {
    s << indent << "DL: ";
    Printer<float>::stream(s, indent + "  ", v.DL);
    s << indent << "DR: ";
    Printer<float>::stream(s, indent + "  ", v.DR);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ROS_RL500XA_MESSAGE_FROMARDUINO_MSG_H

