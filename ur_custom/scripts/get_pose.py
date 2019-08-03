#!/usr/bin/env python

import sys
import moveit_commander
import moveit_msgs.msg
import rospy
import math
import geometry_msgs.msg
import time

if __name__ == "__main__":
	moveit_commander.roscpp_initialize(sys.argv)	
	rospy.init_node("calibrate_camera")
	group = moveit_commander.MoveGroupCommander("manipulator")
	pose = group.get_current_pose()
	print(pose)
