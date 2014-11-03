#ifndef ros_ros_rl500xa_toArduino_msg_h
#define ros_ros_rl500xa_toArduino_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../ros/msg.h"

namespace ros_rl500xa
{

  class toArduino_msg : public ros::Msg
  {
    public:
      long fr_pwm;
      long lr_pwm;
      long turret_pulse_width;
      char * xAxisDirection;
      char * yAxisDirection;
      long movingRobot;

    virtual int serialize(unsigned char *outbuffer)
    {
      int offset = 0;
      union {
        long real;
        unsigned long base;
      } u_fr_pwm;
      u_fr_pwm.real = this->fr_pwm;
      *(outbuffer + offset + 0) = (u_fr_pwm.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_fr_pwm.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_fr_pwm.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_fr_pwm.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->fr_pwm);
      union {
        long real;
        unsigned long base;
      } u_lr_pwm;
      u_lr_pwm.real = this->lr_pwm;
      *(outbuffer + offset + 0) = (u_lr_pwm.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_lr_pwm.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_lr_pwm.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_lr_pwm.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->lr_pwm);
      union {
        long real;
        unsigned long base;
      } u_turret_pulse_width;
      u_turret_pulse_width.real = this->turret_pulse_width;
      *(outbuffer + offset + 0) = (u_turret_pulse_width.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_turret_pulse_width.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_turret_pulse_width.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_turret_pulse_width.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->turret_pulse_width);
      long * length_xAxisDirection = (long *)(outbuffer + offset);
      *length_xAxisDirection = strlen( (const char*) this->xAxisDirection);
      offset += 4;
      memcpy(outbuffer + offset, this->xAxisDirection, *length_xAxisDirection);
      offset += *length_xAxisDirection;
      long * length_yAxisDirection = (long *)(outbuffer + offset);
      *length_yAxisDirection = strlen( (const char*) this->yAxisDirection);
      offset += 4;
      memcpy(outbuffer + offset, this->yAxisDirection, *length_yAxisDirection);
      offset += *length_yAxisDirection;
      union {
        long real;
        unsigned long base;
      } u_movingRobot;
      u_movingRobot.real = this->movingRobot;
      *(outbuffer + offset + 0) = (u_movingRobot.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_movingRobot.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_movingRobot.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_movingRobot.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->movingRobot);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        long real;
        unsigned long base;
      } u_fr_pwm;
      u_fr_pwm.base = 0;
      u_fr_pwm.base |= ((typeof(u_fr_pwm.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_fr_pwm.base |= ((typeof(u_fr_pwm.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_fr_pwm.base |= ((typeof(u_fr_pwm.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_fr_pwm.base |= ((typeof(u_fr_pwm.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->fr_pwm = u_fr_pwm.real;
      offset += sizeof(this->fr_pwm);
      union {
        long real;
        unsigned long base;
      } u_lr_pwm;
      u_lr_pwm.base = 0;
      u_lr_pwm.base |= ((typeof(u_lr_pwm.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_lr_pwm.base |= ((typeof(u_lr_pwm.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_lr_pwm.base |= ((typeof(u_lr_pwm.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_lr_pwm.base |= ((typeof(u_lr_pwm.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->lr_pwm = u_lr_pwm.real;
      offset += sizeof(this->lr_pwm);
      union {
        long real;
        unsigned long base;
      } u_turret_pulse_width;
      u_turret_pulse_width.base = 0;
      u_turret_pulse_width.base |= ((typeof(u_turret_pulse_width.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_turret_pulse_width.base |= ((typeof(u_turret_pulse_width.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_turret_pulse_width.base |= ((typeof(u_turret_pulse_width.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_turret_pulse_width.base |= ((typeof(u_turret_pulse_width.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->turret_pulse_width = u_turret_pulse_width.real;
      offset += sizeof(this->turret_pulse_width);
      uint32_t length_xAxisDirection = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_xAxisDirection; ++k){
          inbuffer[k-1]=inbuffer[k];
           }
      inbuffer[offset+length_xAxisDirection-1]=0;
      this->xAxisDirection = (char *)(inbuffer + offset-1);
      offset += length_xAxisDirection;
      uint32_t length_yAxisDirection = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_yAxisDirection; ++k){
          inbuffer[k-1]=inbuffer[k];
           }
      inbuffer[offset+length_yAxisDirection-1]=0;
      this->yAxisDirection = (char *)(inbuffer + offset-1);
      offset += length_yAxisDirection;
      union {
        long real;
        unsigned long base;
      } u_movingRobot;
      u_movingRobot.base = 0;
      u_movingRobot.base |= ((typeof(u_movingRobot.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_movingRobot.base |= ((typeof(u_movingRobot.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_movingRobot.base |= ((typeof(u_movingRobot.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_movingRobot.base |= ((typeof(u_movingRobot.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->movingRobot = u_movingRobot.real;
      offset += sizeof(this->movingRobot);
     return offset;
    }

    const char * getType(){ return "ros_rl500xa/toArduino_msg"; };

  };

}
#endif