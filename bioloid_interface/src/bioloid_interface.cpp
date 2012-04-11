/*
 * Example
 * Copyright (C) 201
 * 
 */

#include "ros/ros.h"
#include "sensor_msgs/JointState.h"


#include <string>
#include <vector>
#include <math.h>

#include <XmlRpcValue.h>

#include "time.h"

using namespace XmlRpc;
using namespace std;

//These functions get the values from the parameter server and puts them into the vector
void getParamVector_int(ros::NodeHandle, string,vector<int> *);
void getParamVector_double(ros::NodeHandle, string,vector<double> *);
void getParamVector_string(ros::NodeHandle, string,vector<std::string> *);

//Values from the para server.
std::vector<std::string> name;					//Stores joint names
std::vector<int> Servo_number;					//The servo number, used to communicate with servo
std::vector<int> joint_encoder_offset;	//The offset of the servo to make the standard home poistion
std::vector<double> angle_max;					//Max angle, this coulde be used to limit the range of motor
std::vector<double> angle_min;					//Min angle, this coulde be used to limit the range of motor
//Vales to send to the bioloid:
std::vector<double> des_pos; 	//deg
std::vector<double> des_vel;	//deg/sec
//Values to publish:
std::vector<double> pos;	//deg
std::vector<double> vel;	//deg/sec
std::vector<double> eff;	//not used yet, could get motor current.


//This function is called when we recieve a desired message, in the case of the bioloid this is deg or deg/sec
void desiredCallback(const sensor_msgs::JointState::ConstPtr& msg){
	des_pos = msg->position;
	des_vel = msg->velocity;
}

//Main loop.
int main(int argc, char **argv)
{  
  ros::init(argc, argv, "bioloid_interface");
  ros::NodeHandle n("~");
  
  //This is the msg listener and the msg caster.
  ros::Publisher js_pub = n.advertise<sensor_msgs::JointState>("state", 1000);
  ros::Subscriber sub = n.subscribe("command", 1000, desiredCallback);

	/******************************************************************
	*
  * 			Get all the variables from the parameter server.
  *
  ******************************************************************/

  getParamVector_string(n,"/robot_param/head/joints/name",&name);
    
  getParamVector_int(n,"/robot_param/head/joints/cur_max",&Servo_number);
  getParamVector_int(n,"/robot_param/head/joints/cur_min",&joint_encoder_offset);

  getParamVector_double(n,"/robot_param/head/joints/angle_max",&angle_max);     
  getParamVector_double(n,"/robot_param/head/joints/angle_min",&angle_min); 
    
	/******************************************************************
	*
  * 			Connect to bioloid and Setup ROS
  *
  ******************************************************************/

	//Need to do the include to the SDK

  //Communicate at 200hz
  ros::Rate loop_rate(200);
  //Initialice the time.
  ros::Time::init();
	//ROS counter
  int counter = 0;

  ROS_INFO("Number of joints: %d", int(name.size()));
  ROS_INFO("bioloid interface started.");

	/******************************************************************
	*
  * 				Main control loop.
  *
  ******************************************************************/



  while (ros::ok())
  {
    //Send Joint states
   
    counter ++;
    sensor_msgs::JointState js;
    js.header.seq = counter;
    js.header.stamp = ros::Time::now();
    js.header.frame_id = "/world";

        //Used for bedugging, slows down the loops so it prints two times a second
        if(false) {
        	static int skip = 0;
        	if(skip > 100){
        		skip = 0;
            for (unsigned int i = 0 ; i < name.size() ; ++i){
                //ROS_INFO("PWM: %i = %i /  %i", i, head.pwm[i], head.ffc[i]);
            }
        	}else{
        		skip ++;	
        	}
        }
 
        
        
    js.name = name;  
    js.position = pos;
    js.velocity = vel;
    js.effort   = eff;

    js_pub.publish(js);


    ros::spinOnce();
    loop_rate.sleep();
  }
  
  
	/******************************************************************
  *
  * 				Before exit turn everything off.
  *
  ******************************************************************/

  return 0;
}

// Next three functions returns the paramenter server value.

void getParamVector_string(ros::NodeHandle n, string Var,vector<std::string> *Vec){
 
  	XmlRpcValue gainList;
	n.getParam(Var, gainList);
	ROS_ASSERT(gainList.getType() == XmlRpcValue::TypeArray);

	for (int index = 0; index < gainList.size(); index++)
	{
		ROS_ASSERT(gainList[index].getType() == XmlRpcValue::TypeString);
		Vec->push_back(static_cast<std::string>(gainList[index]));
	}
    
}

void getParamVector_int(ros::NodeHandle n, string Var,vector<int> *Vec){
 
  	XmlRpcValue gainList;
	n.getParam(Var, gainList);
	ROS_ASSERT(gainList.getType() == XmlRpcValue::TypeArray);

	for (int index = 0; index < gainList.size(); index++)
	{
		ROS_ASSERT(gainList[index].getType() == XmlRpcValue::TypeInt);
		Vec->push_back(static_cast<int>(gainList[index]));
	}
    
}


void getParamVector_double(ros::NodeHandle n, string Var,vector<double> *Vec){
 
  	XmlRpcValue List;
	n.getParam(Var, List);
	ROS_ASSERT(List.getType() == XmlRpcValue::TypeArray);

	for (int index = 0; index < List.size(); index++)
	{
		ROS_ASSERT(List[index].getType() == XmlRpcValue::TypeDouble);
		Vec->push_back(static_cast<double>(List[index]));
	}
    
}
