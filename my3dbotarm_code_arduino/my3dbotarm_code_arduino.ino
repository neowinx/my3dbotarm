#if defined(ARDUINO) && ARDUINO >= 100
  #include "Arduino.h"
#else
  #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <sensor_msgs/JointState.h>

ros::NodeHandle  nh;
Servo gripper;
Servo wrist_rotate;
Servo wrist_up_down;
Servo elbow;
Servo shoulder;
Servo base;

double base_angle=90;
double shoulder_angle=90;
double elbow_angle=90;
double wrist_up_down_angle=90;
double wrist_rotate_angle=90;
double gripper_angle=90;

void servo_cb(const sensor_msgs::JointState& cmd_msg){
  base_angle=radiansToDegrees(cmd_msg.position[0]);
  shoulder_angle=radiansToDegrees(cmd_msg.position[1]);
  elbow_angle=reverseRadiansToDegrees(cmd_msg.position[2]);
  wrist_up_down_angle=radiansToDegrees(cmd_msg.position[3]);
  wrist_rotate_angle=radiansToDegrees(cmd_msg.position[4]);
  gripper_angle=radiansToDegrees(cmd_msg.position[5]);
  
  base.write(base_angle);
  shoulder.write(shoulder_angle);
  elbow.write(elbow_angle);
  wrist_rotate.write(wrist_rotate_angle);
  wrist_up_down.write(wrist_up_down_angle);
  gripper.write(gripper_angle-15);
  
}


ros::Subscriber<sensor_msgs::JointState> sub("joint_states", servo_cb);

void setup(){
  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub);

  base.attach(7); 
  shoulder.attach(8);
  elbow.attach(9); 
  wrist_rotate.attach(10);
  wrist_up_down.attach(11);
  gripper.attach(12); 

  delay(1);
  base.write(90);
  shoulder.write(90);
  elbow.write(90);
  wrist_rotate.write(90);
  wrist_up_down.write(90);
  gripper.write(90);
}

void loop(){
  nh.spinOnce();
}

double radiansToDegrees(float position_radians)
{
  position_radians = position_radians + 1.6;
  return position_radians * 57.2958;
}

double reverseRadiansToDegrees(float position_radians)
{
  position_radians = position_radians + 1.6;
  position_radians = 3.14159265359 - position_radians
  return position_radians * 57.2958;
}
