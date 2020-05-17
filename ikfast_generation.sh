#!/bin/bash

export MYROBOT_NAME="my3dbotarm"
rosrun xacro xacro -o my3dbotarm_description/urdf/$MYROBOT_NAME.urdf my3dbotarm_description/urdf/$MYROBOT_NAME.xacro
rosrun moveit_kinematics auto_create_ikfast_moveit_plugin.sh --iktype translationdirection5d my3dbotarm_description/urdf/$MYROBOT_NAME.urdf arm base link_05
