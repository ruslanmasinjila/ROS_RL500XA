; Auto-generated. Do not edit!


(cl:in-package ros_rl500xa-msg)


;//! \htmlinclude fromObserver_msg.msg.html

(cl:defclass <fromObserver_msg> (roslisp-msg-protocol:ros-message)
  ((coordinates
    :reader coordinates
    :initarg :coordinates
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (observerID
    :reader observerID
    :initarg :observerID
    :type cl:string
    :initform ""))
)

(cl:defclass fromObserver_msg (<fromObserver_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <fromObserver_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'fromObserver_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_rl500xa-msg:<fromObserver_msg> is deprecated: use ros_rl500xa-msg:fromObserver_msg instead.")))

(cl:ensure-generic-function 'coordinates-val :lambda-list '(m))
(cl:defmethod coordinates-val ((m <fromObserver_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:coordinates-val is deprecated.  Use ros_rl500xa-msg:coordinates instead.")
  (coordinates m))

(cl:ensure-generic-function 'observerID-val :lambda-list '(m))
(cl:defmethod observerID-val ((m <fromObserver_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_rl500xa-msg:observerID-val is deprecated.  Use ros_rl500xa-msg:observerID instead.")
  (observerID m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <fromObserver_msg>) ostream)
  "Serializes a message object of type '<fromObserver_msg>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'coordinates))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'coordinates))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'observerID))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'observerID))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <fromObserver_msg>) istream)
  "Deserializes a message object of type '<fromObserver_msg>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'coordinates) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'coordinates)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'observerID) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'observerID) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<fromObserver_msg>)))
  "Returns string type for a message object of type '<fromObserver_msg>"
  "ros_rl500xa/fromObserver_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'fromObserver_msg)))
  "Returns string type for a message object of type 'fromObserver_msg"
  "ros_rl500xa/fromObserver_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<fromObserver_msg>)))
  "Returns md5sum for a message object of type '<fromObserver_msg>"
  "1cf750dc7f71074725cc226409006b37")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'fromObserver_msg)))
  "Returns md5sum for a message object of type 'fromObserver_msg"
  "1cf750dc7f71074725cc226409006b37")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<fromObserver_msg>)))
  "Returns full string definition for message of type '<fromObserver_msg>"
  (cl:format cl:nil "float32[] coordinates~%string observerID~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'fromObserver_msg)))
  "Returns full string definition for message of type 'fromObserver_msg"
  (cl:format cl:nil "float32[] coordinates~%string observerID~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <fromObserver_msg>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'coordinates) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:length (cl:slot-value msg 'observerID))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <fromObserver_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'fromObserver_msg
    (cl:cons ':coordinates (coordinates msg))
    (cl:cons ':observerID (observerID msg))
))
