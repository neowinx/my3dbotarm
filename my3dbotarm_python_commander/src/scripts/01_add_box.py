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
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
arm_group = moveit_commander.MoveGroupCommander('arm')

rospy.sleep(1)

box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "base"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.y = -0.0
box_pose.pose.position.x = -0.3
box_pose.pose.position.z = 0.05
scene.add_box("box", box_pose, size=(0.05, 0.05, 0.05))

rospy.sleep(1)

grip_pose = geometry_msgs.msg.PoseStamped()
grip_pose.header.frame_id = "base"
grip_pose.pose.orientation.w = box_pose.pose.orientation.w
grip_pose.pose.position.x = box_pose.pose.position.x
grip_pose.pose.position.y = box_pose.pose.position.y
grip_pose.pose.position.z = 0.08

arm_group.set_pose_target(grip_pose)
plan = arm_group.go(wait=True)

rospy.sleep(5)

arm_group.stop()
arm_group.clear_pose_targets()

moveit_commander.roscpp_shutdown()
moveit_commander.os._exit(0)
