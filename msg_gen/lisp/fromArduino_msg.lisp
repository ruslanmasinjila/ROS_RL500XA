; Auto-generated. Do not edit!


(cl:in-package ros_rl500xa-msg)


;//! \htmlinclude fromArduino_msg.msg.html

(cl:defclass <fromArduino_msg> (roslisp-msg-protocol:ros-message)
  ((DL
    :reader DL
    :initarg :DL
    :type cl:float
    :initform 0.0)
   (DR
    :reader DR
    :initarg :DR
    :type cl:float
    :initform 0.0))
)

(cl:defclass fromArduino_msg (<fromArduino_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <fromArduino_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'fromArduino_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_rl500xa-msg:<fromArduino_msg> is deprecated: use ros_rl500xa-msg:fromArduino_msg instead.")))

(cl:ensure-generic-function 'DL-val :lambda-list '(m))
(cl:defmethod DL-val ((m <fromArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:DL-val is deprecated.  Use ros_rl500xa-msg:DL instead.")
  (DL m))

(cl:ensure-generic-function 'DR-val :lambda-list '(m))
(cl:defmethod DR-val ((m <fromArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:DR-val is deprecated.  Use ros_rl500xa-msg:DR instead.")
  (DR m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <fromArduino_msg>) ostream)
  "Serializes a message object of type '<fromArduino_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'DL))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'DR))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <fromArduino_msg>) istream)
  "Deserializes a message object of type '<fromArduino_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'DL) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'DR) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<fromArduino_msg>)))
  "Returns string type for a message object of type '<fromArduino_msg>"
  "ros_rl500xa/fromArduino_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'fromArduino_msg)))
  "Returns string type for a message object of type 'fromArduino_msg"
  "ros_rl500xa/fromArduino_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<fromArduino_msg>)))
  "Returns md5sum for a message object of type '<fromArduino_msg>"
  "523793fd4bc77900491fb58970438a6d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'fromArduino_msg)))
  "Returns md5sum for a message object of type 'fromArduino_msg"
  "523793fd4bc77900491fb58970438a6d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<fromArduino_msg>)))
  "Returns full string definition for message of type '<fromArduino_msg>"
  (cl:format cl:nil "float32 DL~%float32 DR~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'fromArduino_msg)))
  "Returns full string definition for message of type 'fromArduino_msg"
  (cl:format cl:nil "float32 DL~%float32 DR~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <fromArduino_msg>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <fromArduino_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'fromArduino_msg
    (cl:cons ':DL (DL msg))
    (cl:cons ':DR (DR msg))
))
