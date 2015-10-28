#ifndef ros_ros_rl500xa_fromArduino_msg_h
#define ros_ros_rl500xa_fromArduino_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../ros/msg.h"

namespace ros_rl500xa
{

  class fromArduino_msg : public ros::Msg
  {
    public:
      float DL;
      float DR;
      long robotID;

    virtual int serialize(unsigned char *outbuffer)
    {
      int offset = 0;
      union {
        float real;
        unsigned long base;
      } u_DL;
      u_DL.real = this->DL;
      *(outbuffer + offset + 0) = (u_DL.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_DL.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_DL.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_DL.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->DL);
      union {
        float real;
        unsigned long base;
      } u_DR;
      u_DR.real = this->DR;
      *(outbuffer + offset + 0) = (u_DR.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_DR.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_DR.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_DR.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->DR);
      union {
        long real;
        unsigned long base;
      } u_robotID;
      u_robotID.real = this->robotID;
      *(outbuffer + offset + 0) = (u_robotID.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_robotID.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_robotID.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_robotID.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->robotID);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        unsigned long base;
      } u_DL;
      u_DL.base = 0;
      u_DL.base |= ((typeof(u_DL.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_DL.base |= ((typeof(u_DL.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_DL.base |= ((typeof(u_DL.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_DL.base |= ((typeof(u_DL.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->DL = u_DL.real;
      offset += sizeof(this->DL);
      union {
        float real;
        unsigned long base;
      } u_DR;
      u_DR.base = 0;
      u_DR.base |= ((typeof(u_DR.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_DR.base |= ((typeof(u_DR.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_DR.base |= ((typeof(u_DR.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_DR.base |= ((typeof(u_DR.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->DR = u_DR.real;
      offset += sizeof(this->DR);
      union {
        long real;
        unsigned long base;
      } u_robotID;
      u_robotID.base = 0;
      u_robotID.base |= ((typeof(u_robotID.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_robotID.base |= ((typeof(u_robotID.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_robotID.base |= ((typeof(u_robotID.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_robotID.base |= ((typeof(u_robotID.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->robotID = u_robotID.real;
      offset += sizeof(this->robotID);
     return offset;
    }

    const char * getType(){ return "ros_rl500xa/fromArduino_msg"; };

  };

}
#endif