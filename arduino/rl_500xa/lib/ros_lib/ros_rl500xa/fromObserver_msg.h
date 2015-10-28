#ifndef ros_ros_rl500xa_fromObserver_msg_h
#define ros_ros_rl500xa_fromObserver_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../ros/msg.h"

namespace ros_rl500xa
{

  class fromObserver_msg : public ros::Msg
  {
    public:
      unsigned char coordinatesT1_length;
      float st_coordinatesT1;
      float * coordinatesT1;
      unsigned char coordinatesT2_length;
      float st_coordinatesT2;
      float * coordinatesT2;
      char * observerID;

    virtual int serialize(unsigned char *outbuffer)
    {
      int offset = 0;
      *(outbuffer + offset++) = coordinatesT1_length;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      for( unsigned char i = 0; i < coordinatesT1_length; i++){
      union {
        float real;
        unsigned long base;
      } u_coordinatesT1i;
      u_coordinatesT1i.real = this->coordinatesT1[i];
      *(outbuffer + offset + 0) = (u_coordinatesT1i.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_coordinatesT1i.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_coordinatesT1i.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_coordinatesT1i.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->coordinatesT1[i]);
      }
      *(outbuffer + offset++) = coordinatesT2_length;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      *(outbuffer + offset++) = 0;
      for( unsigned char i = 0; i < coordinatesT2_length; i++){
      union {
        float real;
        unsigned long base;
      } u_coordinatesT2i;
      u_coordinatesT2i.real = this->coordinatesT2[i];
      *(outbuffer + offset + 0) = (u_coordinatesT2i.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_coordinatesT2i.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_coordinatesT2i.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_coordinatesT2i.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->coordinatesT2[i]);
      }
      long * length_observerID = (long *)(outbuffer + offset);
      *length_observerID = strlen( (const char*) this->observerID);
      offset += 4;
      memcpy(outbuffer + offset, this->observerID, *length_observerID);
      offset += *length_observerID;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      unsigned char coordinatesT1_lengthT = *(inbuffer + offset++);
      if(coordinatesT1_lengthT > coordinatesT1_length)
        this->coordinatesT1 = (float*)realloc(this->coordinatesT1, coordinatesT1_lengthT * sizeof(float));
      offset += 3;
      coordinatesT1_length = coordinatesT1_lengthT;
      for( unsigned char i = 0; i < coordinatesT1_length; i++){
      union {
        float real;
        unsigned long base;
      } u_st_coordinatesT1;
      u_st_coordinatesT1.base = 0;
      u_st_coordinatesT1.base |= ((typeof(u_st_coordinatesT1.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_coordinatesT1.base |= ((typeof(u_st_coordinatesT1.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_coordinatesT1.base |= ((typeof(u_st_coordinatesT1.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_coordinatesT1.base |= ((typeof(u_st_coordinatesT1.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_coordinatesT1 = u_st_coordinatesT1.real;
      offset += sizeof(this->st_coordinatesT1);
        memcpy( &(this->coordinatesT1[i]), &(this->st_coordinatesT1), sizeof(float));
      }
      unsigned char coordinatesT2_lengthT = *(inbuffer + offset++);
      if(coordinatesT2_lengthT > coordinatesT2_length)
        this->coordinatesT2 = (float*)realloc(this->coordinatesT2, coordinatesT2_lengthT * sizeof(float));
      offset += 3;
      coordinatesT2_length = coordinatesT2_lengthT;
      for( unsigned char i = 0; i < coordinatesT2_length; i++){
      union {
        float real;
        unsigned long base;
      } u_st_coordinatesT2;
      u_st_coordinatesT2.base = 0;
      u_st_coordinatesT2.base |= ((typeof(u_st_coordinatesT2.base)) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_coordinatesT2.base |= ((typeof(u_st_coordinatesT2.base)) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_coordinatesT2.base |= ((typeof(u_st_coordinatesT2.base)) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_coordinatesT2.base |= ((typeof(u_st_coordinatesT2.base)) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_coordinatesT2 = u_st_coordinatesT2.real;
      offset += sizeof(this->st_coordinatesT2);
        memcpy( &(this->coordinatesT2[i]), &(this->st_coordinatesT2), sizeof(float));
      }
      uint32_t length_observerID = *(uint32_t *)(inbuffer + offset);
      offset += 4;
      for(unsigned int k= offset; k< offset+length_observerID; ++k){
          inbuffer[k-1]=inbuffer[k];
           }
      inbuffer[offset+length_observerID-1]=0;
      this->observerID = (char *)(inbuffer + offset-1);
      offset += length_observerID;
     return offset;
    }

    const char * getType(){ return "ros_rl500xa/fromObserver_msg"; };

  };

}
#endif