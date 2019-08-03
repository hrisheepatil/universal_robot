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

class captureSend():

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
        			cv2.imwrite('template_images/template_image'+str(self.count)+'.jpeg', cv2_img)

       	 	except rospy.ServiceException, e:
        		print ("Service call failed: %s"%e)

	def move_robot(self):
		time.sleep(1)
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.5
		pose_goal.orientation.y = 0.5
		pose_goal.orientation.z = -0.5
		pose_goal.orientation.w = 0.5
		pose_goal.position.x = 0.5
		pose_goal.position.y = 0.0
		pose_goal.position.z = 0.7
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.405121334605
		pose_goal.orientation.y = 0.579150181123
		pose_goal.orientation.z = -0.579640476419
		pose_goal.orientation.w = 0.405559724393
		pose_goal.position.x = 0.499953222727
		pose_goal.position.y = 8.21067371154e-05
		pose_goal.position.z = 0.700069869403
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.589145590692
		pose_goal.orientation.y = 0.390363546429
		pose_goal.orientation.z = -0.390636495506
		pose_goal.orientation.w = 0.589853289358
		pose_goal.position.x = 0.464620808126
		pose_goal.position.y = 2.96766855797e-05
		pose_goal.position.z = 0.685100763662
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.591440226239
		pose_goal.orientation.y = 0.590847578967
		pose_goal.orientation.z = -0.387900889591
		pose_goal.orientation.w = 0.388111449291
		pose_goal.position.x = 0.500077914386
		pose_goal.position.y = 7.94030828376e-06
		pose_goal.position.z = 0.700028601138
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.34904777697
		pose_goal.orientation.y = 0.348407395499
		pose_goal.orientation.z = -0.615002061271
		pose_goal.orientation.w = 0.615264496607
		pose_goal.position.x = 0.500016399229
		pose_goal.position.y = 0.0122583542623
		pose_goal.position.z = 0.692604537495
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.520050247899
		pose_goal.orientation.y = 0.519581506703
		pose_goal.orientation.z = -0.479116588687
		pose_goal.orientation.w = 0.479614524381
		pose_goal.position.x = 0.481639426752
		pose_goal.position.y = 0.0149425701572
		pose_goal.position.z = 0.659279578341
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.442475740035
		pose_goal.orientation.y = 0.441879969174
		pose_goal.orientation.z = -0.551520428019
		pose_goal.orientation.w = 0.552071127483
		pose_goal.position.x = 0.481719214119
		pose_goal.position.y = 0.0149882320268
		pose_goal.position.z = 0.659353271698
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.54457720204
		pose_goal.orientation.y = 0.544173605843
		pose_goal.orientation.z = -0.450972678487
		pose_goal.orientation.w = 0.451590966452
		pose_goal.position.x = 0.481562754094
		pose_goal.position.y = 0.00334704455184
		pose_goal.position.z = 0.72103444814
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
	
	def learn_obj(self):
		img = cv2.imread('template_images/template_image1.jpeg')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
		edged = cv2.Canny(gray, 30, 200) 
		a, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 	
		cnt = contours[0]
    		cv2.waitKey(0)	

if __name__ == "__main__":
	moveit_commander.roscpp_initialize(sys.argv)	
	rospy.init_node("learn_object")
	time.sleep(2)
	cs = captureSend()
#	cs.move_robot()
	cs.learn_obj()
