#include <Arduino.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <ros_rl500xa/fromArduino_msg.h>
#include <ros_rl500xa/toArduino_msg.h>
#include <Servo.h> 
void setup();
void loop();
void publishEncoderDistances();
void steerPlatform();
void forwardReversePWM();
void leftRightPWM();
void differentialSteering();
int pwmDifference(int fr_pwm, int lr_pwm);
void stopDrivingMotors();
void stopReverse();
void stopFoward();
void leftEncoderISR();
void rightEncoderISR();
void turn_turret();
#line 1 "src/rl_500xa.ino"
//**********************************HEADERS***********************************
//#include <ros.h>
//#include <std_msgs/String.h>
//#include <ros_rl500xa/fromArduino_msg.h>
//#include <ros_rl500xa/toArduino_msg.h>
//#include <Servo.h> 


//**********************************PROTOTYPES***********************************

//ROS prototypes
void arduinoCommands_cb(const ros_rl500xa::toArduino_msg &ardCmd);
void publishEncoderDistances();

//RC prototypes
void steerPlatform();
void forwardReversePWM();
void leftRightPWM();
void differentialSteering();
void keyboardSteering(char* const direction);
int  pwmDifference(int fr_pwm, int lr_pwm);
void stopDrivingMotors();
void stopReverse();
void stopFoward();

//Interrupt Prototypes
void leftEncoderISR();
void rightEncoderISR();

//Turret Prototypes
void turn_turret();


//********************************ROS variables*********************************

//Create node handle
ros::NodeHandle nh;

//String message
std_msgs::String str_msg;

//Custom rl500xa messages
ros_rl500xa::fromArduino_msg fromArduino_msg;


//Create ROS publisher
ros::Publisher arduinoToROS_pub("arduinoToROS_tpc", &fromArduino_msg);

//Create ROS Subscriber
ros::Subscriber<ros_rl500xa::toArduino_msg> arduinoCommands_sub("ROSToArduino_tpc", arduinoCommands_cb);



//*****************************RC VARIABLES*********************************
//Channel 2 RC Signal. Signal considered lost below 900
int SIGNAL_THRESHOLD=900;            

//0 if there is no signal, 1 if there is connection 
int RC_CONNECTION_STATUS=0;


//Channel 2 Pulse widths (in microseconds)
//Up=Forward
//Down=Reverse

int FORWARD_MIN=1500;                
int FORWARD_MAX=1800;              

int REVERSE_MIN=1300;                
int REVERSE_MAX=1000;   

//Channel 2 digital pins
int CH2_PIN=52;                     
int CH4_PIN=53;                       

//Holds the duration, in microseconds, of the pulse from channel 2 when the signal is HIGH
//Forward: ch2_rc>=1500. Set any value>=1800 to 1800
//Reverse: ch2_rc<=1300. Set any value<=1000 to 1000
//Stop: All remaining ch2_rc values
int ch2_rc;                         

//Channel 4 Widths
//Left=left 
//Right=right
   
int LEFT_MIN=1700;                
int LEFT_MAX=1900;              

int RIGHT_MIN=1500;                
int RIGHT_MAX=1300;   

//Holds the duration, in microseconds, of the pulse from channel 3 when the signal is HIGH
//Left: ch4_rc>=1700. Set any value>=1900 to 1900
//Right: ch4_rc<=1500. Set any value<=1300 to 1300
//Straight: All remaining ch4_rc values
int ch4_rc;                            


//Holds the PWM value for forward and reverse
int fr_pwm=0;                       
 
//Holds the PWM value for left and right
int lr_pwm=0;                       

//Minimum Speed
int PWM_MIN=0;                      

//Maximum Speed (RC mode)
int PWM_MAX=254;

//Maximum Speed (Keyboard mode)
int PWM_MAX_KEY=50;                    


//PWM PINS on MegaMoto: 3,5,6,9,10,11
//Pin  5 drives the LEFT  MOTOR in the REVERSE DIRECTION
//Pin  6 drives the LEFT  MOTOR in the FORWARD DIRECTION
//Pin  9 drives the RIGHT MOTOR in the FORWARD DIRECTION
//Pin 10 drives the RIGHT MOTOR in the REVERSE DIRECTION
int LEFT_MOTOR_FOWARD_PIN=6;
int LEFT_MOTOR_REVERSE_PIN=5;
int RIGHT_MOTOR_FOWARD_PIN=9;
int RIGHT_MOTOR_REVERSE_PIN=10;


//ENABLE_PIN Pins on MegaMoto: 8,12,13 and 5V(Always On)
//Shields are enabled by HIGH signal on Pin 8, disabled by LOW signal
//Place jumpers on all Shields on D8
int ENABLE_PIN=8;


//Holds the yAxisDirection direction of the motors (Forward='f', Reverse='r') in RC mode
char yAxisDirection='\0';
char xAxisDirection='\0';


//*****************************ENCODER VARIABLES*********************************
//Best Results obtained when:
//1. Encoder pcb is 1cm from the reflective surface
//2. Debounce time is 2 milliseconds

int LEFT_ENCODER_INTERRUPT=0;	//On Digital Pin 2 of Arduino 
int RIGHT_ENCODER_INTERRUPT=1;	//On Digital Pin 3 of Arduino

//Encoder Counts [Black and White Stripes]
int leftEncoderCount=0;
int rightEncoderCount=0;

//Debounce time
int debounce_time=3;


//*****************************TURRET VARIABLES*********************************
Servo turret;
int turret_pin=22;
int turret_pulse_width=1500;

//********************************ROBOT VARIABLES*********************************
int robotID=0;
int allRobots=999;
int movingRobot=-1;
//**********************************SETUP***********************************
void setup()
{

//Initialize this node, publish and subscribe to topics
nh.initNode();
nh.advertise(arduinoToROS_pub);
nh.subscribe(arduinoCommands_sub);

//Initialize Motor shields for Arduino (MegaMoto shields)
pinMode(CH2_PIN, INPUT);
pinMode(CH4_PIN, INPUT);

//ENABLE MOTOR SHIELDS
pinMode(ENABLE_PIN,OUTPUT);
digitalWrite(ENABLE_PIN,HIGH);

//STOP ALL MOTORS
analogWrite(RIGHT_MOTOR_FOWARD_PIN,0);
analogWrite(RIGHT_MOTOR_REVERSE_PIN,0);

analogWrite(LEFT_MOTOR_FOWARD_PIN,0);
analogWrite(LEFT_MOTOR_REVERSE_PIN,0);

//ATTACH ENCODER INTERRUPTS
attachInterrupt(LEFT_ENCODER_INTERRUPT,leftEncoderISR,CHANGE);
attachInterrupt(RIGHT_ENCODER_INTERRUPT,rightEncoderISR,CHANGE);

//ATTACH SERVO
turret.attach(turret_pin);
turret.writeMicroseconds(1500);



}


//**********************************MAIN LOOP***********************************
void loop()
{

    nh.spinOnce();

    //Steer the selected platform
    if(movingRobot==robotID||movingRobot==allRobots)
    {
    steerPlatform();
    }
    turn_turret();
    publishEncoderDistances();

}
//**********************************ROS FUNCTIONS***********************************
void arduinoCommands_cb(const ros_rl500xa::toArduino_msg &ardCmd)
{

	//Platform Steering commands
	fr_pwm=ardCmd.fr_pwm;
	lr_pwm=ardCmd.lr_pwm;

	xAxisDirection=*ardCmd.xAxisDirection;
	yAxisDirection=*ardCmd.yAxisDirection;

	//Turret Steering Commands
	turret_pulse_width=ardCmd.turret_pulse_width;

	//Robot Selection Commands
	movingRobot=ardCmd.movingRobot;
	
}
void publishEncoderDistances()
{
    fromArduino_msg.DL=leftEncoderCount;
    fromArduino_msg.DR=rightEncoderCount;
    arduinoToROS_pub.publish(&fromArduino_msg);
}
//****************************RC FUNCTIONS***************************
//Converts RC Signals or Keyboard commands to PWM pulses which are used to diver the motors
void steerPlatform()
{
    //Default RC_CONNECTION_STATUS is 0
    if(RC_CONNECTION_STATUS==1)
    {
        forwardReversePWM();
        leftRightPWM();
    }
    differentialSteering();
}
//Reads the RC signal from Channel 2
//Converts the RC signal to corresponding PWM value (0-254)
void forwardReversePWM()
{
    ch2_rc = pulseIn(CH2_PIN, HIGH);
    //If the Motors are moving in the forward Direction
    if(ch2_rc>=FORWARD_MIN )
    {
        if(ch2_rc>=FORWARD_MAX)
        {
            ch2_rc=FORWARD_MAX;
        }
        fr_pwm = map(ch2_rc, FORWARD_MIN , FORWARD_MAX, PWM_MIN, PWM_MAX);
        yAxisDirection='f';
    }
    //If the Motors are moving in the reverse Direction
    else if(ch2_rc>SIGNAL_THRESHOLD&&ch2_rc<=REVERSE_MIN)
    {
        if(ch2_rc<=REVERSE_MAX)
        {
            ch2_rc=REVERSE_MAX;
        }
        fr_pwm = map(ch2_rc, REVERSE_MIN, REVERSE_MAX, PWM_MIN, PWM_MAX);
        yAxisDirection='b';
    }
    else
    {
        fr_pwm=0;
    }
}
//Reads RC Signal from Channel 4.
//Converts the RC Signal to corresponding PWM value (0-254)
void leftRightPWM()
{
    ch4_rc = pulseIn(CH4_PIN, HIGH);
    //If the Motors are moving in the left Direction
    if(ch4_rc>=LEFT_MIN )
    {
        if(ch4_rc>=LEFT_MAX)
        {
            ch4_rc=LEFT_MAX;
        }
        lr_pwm = map(ch4_rc, LEFT_MIN , LEFT_MAX, PWM_MIN, PWM_MAX);
        xAxisDirection='l';
    }
    //If the Motors are moving in the reverse Direction
    //Must be strictly greater than SIGNAL_THRESHOLD (0)
    else if(ch4_rc<=RIGHT_MIN)
    {
        if(ch4_rc<=RIGHT_MAX)
        {
            ch4_rc=RIGHT_MAX;
        }
        lr_pwm = map(ch4_rc, RIGHT_MIN, RIGHT_MAX, PWM_MIN, PWM_MAX);
        xAxisDirection='r';
    }
    else
    {
        lr_pwm=0;
    }
}
//Differential Steering
void differentialSteering()
{
    int pwm_difference=0;
    pwm_difference=pwmDifference(fr_pwm,lr_pwm);
    if(fr_pwm==0)
    {
        stopDrivingMotors();
    }
    if(yAxisDirection=='f')
    {
        stopReverse();
    }
    if(yAxisDirection=='b')
    {
        stopFoward();
    }
    if(yAxisDirection=='f'&& xAxisDirection=='l')
    {
        analogWrite(RIGHT_MOTOR_FOWARD_PIN,fr_pwm);
        analogWrite(LEFT_MOTOR_FOWARD_PIN,pwm_difference);
    }
    if(yAxisDirection=='f'&& xAxisDirection=='r')
    {
        analogWrite(LEFT_MOTOR_FOWARD_PIN,fr_pwm);
        analogWrite(RIGHT_MOTOR_FOWARD_PIN,pwm_difference);
    }
    if(yAxisDirection=='b'&& xAxisDirection=='l')
    {
        analogWrite(RIGHT_MOTOR_REVERSE_PIN,fr_pwm);
        analogWrite(LEFT_MOTOR_REVERSE_PIN,pwm_difference);
    }
    if (yAxisDirection=='b'&& xAxisDirection=='r')
    {
        analogWrite(LEFT_MOTOR_REVERSE_PIN,fr_pwm);
        analogWrite(RIGHT_MOTOR_REVERSE_PIN,pwm_difference);
    }
    if(yAxisDirection=='f'&& xAxisDirection=='\0')
    {
        analogWrite(RIGHT_MOTOR_FOWARD_PIN,fr_pwm);
        analogWrite(LEFT_MOTOR_FOWARD_PIN,fr_pwm);
    }
    if (yAxisDirection=='b'&& xAxisDirection=='\0')
    {
        analogWrite(RIGHT_MOTOR_REVERSE_PIN,fr_pwm);
        analogWrite(LEFT_MOTOR_REVERSE_PIN,fr_pwm);
    }
    xAxisDirection='\0';
    yAxisDirection='\0';
}
/*
void keyboardSteering(char* const direction)
{
    String dir=direction;
    if(dir.equals("forward"))
    {
        stopReverse();
        analogWrite(RIGHT_MOTOR_FOWARD_PIN,PWM_MAX_KEY);
        analogWrite(LEFT_MOTOR_FOWARD_PIN,PWM_MAX_KEY);
    }
    else if(dir.equals("reverse"))
    {
        stopFoward();
        analogWrite(RIGHT_MOTOR_REVERSE_PIN,PWM_MAX_KEY);
        analogWrite(LEFT_MOTOR_REVERSE_PIN,PWM_MAX_KEY);
    }
    else if (dir.equals("left"))
    {
        analogWrite(RIGHT_MOTOR_REVERSE_PIN,0);
        analogWrite(RIGHT_MOTOR_FOWARD_PIN,PWM_MAX_KEY);
        analogWrite(LEFT_MOTOR_FOWARD_PIN,0);
        analogWrite(LEFT_MOTOR_REVERSE_PIN,PWM_MAX_KEY);
    }
    else if (dir.equals("right"))
    {
        analogWrite(LEFT_MOTOR_REVERSE_PIN,0);
        analogWrite(LEFT_MOTOR_FOWARD_PIN,PWM_MAX_KEY);
        analogWrite(RIGHT_MOTOR_FOWARD_PIN,0);
        analogWrite(RIGHT_MOTOR_REVERSE_PIN,PWM_MAX_KEY);
    }
    else
    {
        stopFoward();
        stopReverse();
    }
}*/
int pwmDifference(int fr_pwm, int lr_pwm)
{
    int difference=fr_pwm-lr_pwm;
    if(difference<=0)
    {
        difference=0;
    }
    return difference;
}
//Stops the driving Motors (Left and Right Wheels) by sending 0 PWM to both Motors.
void stopDrivingMotors()
{
    stopReverse();
    stopFoward();
}
void stopReverse()
{
    analogWrite(RIGHT_MOTOR_REVERSE_PIN,0);
    analogWrite(LEFT_MOTOR_REVERSE_PIN,0);
}
void stopFoward()
{
    analogWrite(RIGHT_MOTOR_FOWARD_PIN,0);
    analogWrite(LEFT_MOTOR_FOWARD_PIN,0);
}
//*****************************ENCODER FUNCTIONS*********************************

//Interrupt Service Routine for the Left encoder
void leftEncoderISR()
{
  static unsigned long last_interrupt_time_left = 0;
  unsigned long interrupt_time_left = millis();
  if (interrupt_time_left - last_interrupt_time_left > debounce_time) 
  {
    leftEncoderCount+=1;
  }
  last_interrupt_time_left = interrupt_time_left;
}

//Interrupt Service Routine for the Right encoder
void rightEncoderISR()
{
  static unsigned long last_interrupt_time_right = 0;
  unsigned long interrupt_time_right = millis();
  if (interrupt_time_right - last_interrupt_time_right > debounce_time) 
  {
    rightEncoderCount+=1;
  }
  last_interrupt_time_right = interrupt_time_right;
}

//*****************************ENCODER FUNCTIONS*********************************
void turn_turret()
{
turret.writeMicroseconds(turret_pulse_width);

}

