#!/usr/bin/env python

import sys
import copy
import moveit_commander
import moveit_msgs.msg
import rospy
import math
import geometry_msgs.msg
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from ur_custom.srv import CaptureImageResponse
from ur_custom.srv import CaptureImageRequest
from ur_custom.srv import CaptureImage

def capture_send():
	rospy.wait_for_service('capture_image')
	try:
		capture_image = rospy.ServiceProxy('capture_image', CaptureImage)
		resp = CaptureImageRequest()
         	resp.capture = 1
		capture_image(resp)
		return resp.done

        except rospy.ServiceException, e:
        	print ("Service call failed: %s"%e)

if __name__ == "__main__":
	moveit_commander.roscpp_initialize(sys.argv)	
	rospy.init_node("robot_control_ur")
	group = moveit_commander.MoveGroupCommander("manipulator")
	pose = group.get_current_pose().pose
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.5
	pose_goal.orientation.y = 0.5
	pose_goal.orientation.z = -0.5
	pose_goal.orientation.w = 0.5
	pose_goal.position.x = 0.50
	pose_goal.position.y = 0.0
	pose_goal.position.z = 0.7
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.5
	pose_goal.orientation.y = 0.5
	pose_goal.orientation.z = -0.5
	pose_goal.orientation.w = 0.5
	pose_goal.position.x = 0.0
	pose_goal.position.y = -0.5
	pose_goal.position.z = 0.7
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.5
	pose_goal.orientation.y = 0.5
	pose_goal.orientation.z = -0.5
	pose_goal.orientation.w = 0.5
	pose_goal.position.x = -0.50
	pose_goal.position.y = 0.0
	pose_goal.position.z = 0.7
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
	recv = capture_send()
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.291558964145
	pose_goal.orientation.y = 0.291057470962
	pose_goal.orientation.z = -0.644337178617
	pose_goal.orientation.w = 0.644289158123
	pose_goal.position.x = -0.550003824433
	pose_goal.position.y = 0.0410436404787
	pose_goal.position.z = 0.663785858288
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.605613239458
	pose_goal.orientation.y = 0.314254944388
	pose_goal.orientation.z = -0.653215458798
	pose_goal.orientation.w = 0.328307780152
	pose_goal.position.x = -0.518497985519
	pose_goal.position.y = 0.0334208906592
	pose_goal.position.z = 0.646199832625
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.481541011588
	pose_goal.orientation.y = 0.493296125559
	pose_goal.orientation.z = -0.530992374693
	pose_goal.orientation.w = 0.492772041299
	pose_goal.position.x = -0.515962875117
	pose_goal.position.y = 0.0170530677943
	pose_goal.position.z = 0.704129299506
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.665295824139
	pose_goal.orientation.y = 0.569565994532
	pose_goal.orientation.z = -0.334927430103
	pose_goal.orientation.w = 0.347562455999
	pose_goal.position.x = -0.559115992737
	pose_goal.position.y = -0.0521707920078
	pose_goal.position.z = 0.630004141186
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.637441729664
	pose_goal.orientation.y = 0.600720160124
	pose_goal.orientation.z = -0.350972489186
	pose_goal.orientation.w = 0.331091592068
	pose_goal.position.x = -0.562589356589
	pose_goal.position.y = -0.0549348779807
	pose_goal.position.z = 0.634726138665
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.494692899603
	pose_goal.orientation.y = 0.466016201817
	pose_goal.orientation.z = -0.533793658933
	pose_goal.orientation.w = 0.503162165122
	pose_goal.position.x = -0.559555909591
	pose_goal.position.y = -0.00464149569069
	pose_goal.position.z = 0.651925908999
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.535547257025
	pose_goal.orientation.y = 0.50469426486
	pose_goal.orientation.z = -0.492806308614
	pose_goal.orientation.w = 0.464343382312
	pose_goal.position.x = -0.558637172538
	pose_goal.position.y = 0.0121109409529
	pose_goal.position.z = 0.658053695701
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
        pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.5
	pose_goal.orientation.y = 0.5
	pose_goal.orientation.z = -0.5
	pose_goal.orientation.w = 0.5
	pose_goal.position.x = -0.50
	pose_goal.position.y = 0.0
	pose_goal.position.z = 0.7
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
	pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.5
	pose_goal.orientation.y = 0.5
	pose_goal.orientation.z = -0.5
	pose_goal.orientation.w = 0.5
	pose_goal.position.x = 0.0
	pose_goal.position.y = -0.5
	pose_goal.position.z = 0.7
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
	pose_goal = geometry_msgs.msg.Pose()
	pose_goal.orientation.x = 0.5
	pose_goal.orientation.y = 0.5
	pose_goal.orientation.z = -0.5
	pose_goal.orientation.w = 0.5
	pose_goal.position.x = 0.50
	pose_goal.position.y = 0.0
	pose_goal.position.z = 0.7
	group.set_pose_target(pose_goal)
	group.go(pose_goal, wait=True)
	group.stop()
        time.sleep(1)
	#rospy.spin()
