; Auto-generated. Do not edit!


(cl:in-package ros_rl500xa-msg)


;//! \htmlinclude toArduino_msg.msg.html

(cl:defclass <toArduino_msg> (roslisp-msg-protocol:ros-message)
  ((fr_pwm
    :reader fr_pwm
    :initarg :fr_pwm
    :type cl:integer
    :initform 0)
   (lr_pwm
    :reader lr_pwm
    :initarg :lr_pwm
    :type cl:integer
    :initform 0)
   (turret_pulse_width
    :reader turret_pulse_width
    :initarg :turret_pulse_width
    :type cl:integer
    :initform 0)
   (xAxisDirection
    :reader xAxisDirection
    :initarg :xAxisDirection
    :type cl:string
    :initform "")
   (yAxisDirection
    :reader yAxisDirection
    :initarg :yAxisDirection
    :type cl:string
    :initform "")
   (movingRobot
    :reader movingRobot
    :initarg :movingRobot
    :type cl:integer
    :initform 0)
   (sendEncoderData
    :reader sendEncoderData
    :initarg :sendEncoderData
    :type cl:integer
    :initform 0)
   (resetEncoders
    :reader resetEncoders
    :initarg :resetEncoders
    :type cl:integer
    :initform 0))
)

(cl:defclass toArduino_msg (<toArduino_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <toArduino_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'toArduino_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_rl500xa-msg:<toArduino_msg> is deprecated: use ros_rl500xa-msg:toArduino_msg instead.")))

(cl:ensure-generic-function 'fr_pwm-val :lambda-list '(m))
(cl:defmethod fr_pwm-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:fr_pwm-val is deprecated.  Use ros_rl500xa-msg:fr_pwm instead.")
  (fr_pwm m))

(cl:ensure-generic-function 'lr_pwm-val :lambda-list '(m))
(cl:defmethod lr_pwm-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:lr_pwm-val is deprecated.  Use ros_rl500xa-msg:lr_pwm instead.")
  (lr_pwm m))

(cl:ensure-generic-function 'turret_pulse_width-val :lambda-list '(m))
(cl:defmethod turret_pulse_width-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:turret_pulse_width-val is deprecated.  Use ros_rl500xa-msg:turret_pulse_width instead.")
  (turret_pulse_width m))

(cl:ensure-generic-function 'xAxisDirection-val :lambda-list '(m))
(cl:defmethod xAxisDirection-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:xAxisDirection-val is deprecated.  Use ros_rl500xa-msg:xAxisDirection instead.")
  (xAxisDirection m))

(cl:ensure-generic-function 'yAxisDirection-val :lambda-list '(m))
(cl:defmethod yAxisDirection-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:yAxisDirection-val is deprecated.  Use ros_rl500xa-msg:yAxisDirection instead.")
  (yAxisDirection m))

(cl:ensure-generic-function 'movingRobot-val :lambda-list '(m))
(cl:defmethod movingRobot-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:movingRobot-val is deprecated.  Use ros_rl500xa-msg:movingRobot instead.")
  (movingRobot m))

(cl:ensure-generic-function 'sendEncoderData-val :lambda-list '(m))
(cl:defmethod sendEncoderData-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:sendEncoderData-val is deprecated.  Use ros_rl500xa-msg:sendEncoderData instead.")
  (sendEncoderData m))

(cl:ensure-generic-function 'resetEncoders-val :lambda-list '(m))
(cl:defmethod resetEncoders-val ((m <toArduino_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:resetEncoders-val is deprecated.  Use ros_rl500xa-msg:resetEncoders instead.")
  (resetEncoders m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <toArduino_msg>) ostream)
  "Serializes a message object of type '<toArduino_msg>"
  (cl:let* ((signed (cl:slot-value msg 'fr_pwm)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'lr_pwm)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'turret_pulse_width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'xAxisDirection))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'xAxisDirection))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'yAxisDirection))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'yAxisDirection))
  (cl:let* ((signed (cl:slot-value msg 'movingRobot)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'sendEncoderData)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'resetEncoders)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <toArduino_msg>) istream)
  "Deserializes a message object of type '<toArduino_msg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fr_pwm) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'lr_pwm) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'turret_pulse_width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'xAxisDirection) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'xAxisDirection) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yAxisDirection) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'yAxisDirection) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'movingRobot) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sendEncoderData) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'resetEncoders) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<toArduino_msg>)))
  "Returns string type for a message object of type '<toArduino_msg>"
  "ros_rl500xa/toArduino_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'toArduino_msg)))
  "Returns string type for a message object of type 'toArduino_msg"
  "ros_rl500xa/toArduino_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<toArduino_msg>)))
  "Returns md5sum for a message object of type '<toArduino_msg>"
  "f91b4a8598aa3fa9c07c3c68c4411337")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'toArduino_msg)))
  "Returns md5sum for a message object of type 'toArduino_msg"
  "f91b4a8598aa3fa9c07c3c68c4411337")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<toArduino_msg>)))
  "Returns full string definition for message of type '<toArduino_msg>"
  (cl:format cl:nil "int32 fr_pwm~%int32 lr_pwm~%int32 turret_pulse_width~%string xAxisDirection~%string yAxisDirection~%int32 movingRobot~%int32 sendEncoderData~%int32 resetEncoders~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'toArduino_msg)))
  "Returns full string definition for message of type 'toArduino_msg"
  (cl:format cl:nil "int32 fr_pwm~%int32 lr_pwm~%int32 turret_pulse_width~%string xAxisDirection~%string yAxisDirection~%int32 movingRobot~%int32 sendEncoderData~%int32 resetEncoders~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <toArduino_msg>))
  (cl:+ 0
     4
     4
     4
     4 (cl:length (cl:slot-value msg 'xAxisDirection))
     4 (cl:length (cl:slot-value msg 'yAxisDirection))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <toArduino_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'toArduino_msg
    (cl:cons ':fr_pwm (fr_pwm msg))
    (cl:cons ':lr_pwm (lr_pwm msg))
    (cl:cons ':turret_pulse_width (turret_pulse_width msg))
    (cl:cons ':xAxisDirection (xAxisDirection msg))
    (cl:cons ':yAxisDirection (yAxisDirection msg))
    (cl:cons ':movingRobot (movingRobot msg))
    (cl:cons ':sendEncoderData (sendEncoderData msg))
    (cl:cons ':resetEncoders (resetEncoders msg))
))
