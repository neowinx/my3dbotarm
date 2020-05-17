#/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('moveit_pick_test')
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "base_link"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.x = 0.2
box_pose.pose.position.y = 0.2
box_pose.pose.position.z = 0.05
scene.add_box("box", box_pose, size=(0.1, 0.1, 0.1))

moveit_commander.roscpp_shutdown()
moveit_commander.os._exit(0)
