
(cl:in-package :asdf)

(defsystem "ros_rl500xa-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "toArduino_msg" :depends-on ("_package_toArduino_msg"))
    (:file "_package_toArduino_msg" :depends-on ("_package"))
    (:file "fromArduino_msg" :depends-on ("_package_fromArduino_msg"))
    (:file "_package_fromArduino_msg" :depends-on ("_package"))
  ))