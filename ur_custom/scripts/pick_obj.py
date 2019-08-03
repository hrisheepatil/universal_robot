#!/usr/bin/env python

import sys
import copy
import moveit_commander
import moveit_msgs.msg
import rospy
import math
import geometry_msgs.msg
import time
import numpy as np
from matplotlib import pyplot as plt
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from ur_custom.srv import CaptureImageResponse
from ur_custom.srv import CaptureImageRequest
from ur_custom.srv import CaptureImage

bridge = CvBridge()

class pickObject():

	def __init__(self):
#		self.capture_image = rospy.ServiceProxy('capture_image', CaptureImage)
#		self.group = moveit_commander.MoveGroupCommander("manipulator") 
		self.count = 0

	def process(self):
		rospy.wait_for_service('capture_image')
		try:		
			resp = CaptureImageRequest()
         		resp.capture = 1
			res = self.capture_image(resp)
			try:
       				cv2_img = bridge.imgmsg_to_cv2(res.image, "bgr8")
			except CvBridgeError, e:
        			print(e)
    			else:
				self.count = self.count + 1 
        			cv2.imwrite('object_scene/object_image'+str(self.count)+'.jpeg', cv2_img)

       	 	except rospy.ServiceException, e:
        		print ("Service call failed: %s"%e)

	def move_robot(self):
		time.sleep(1)
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.5
		pose_goal.orientation.y = 0.5
		pose_goal.orientation.z = -0.5
		pose_goal.orientation.w = 0.5
		pose_goal.position.x = -0.02
		pose_goal.position.y = -0.5
		pose_goal.position.z = 0.8
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()

	def proccess_image(self):
		

if __name__ == "__main__":
	moveit_commander.roscpp_initialize(sys.argv)	
	rospy.init_node("pick_object")
	time.sleep(2)
	po = pickObject()
#	po.move_robot()
	po.process_image()
