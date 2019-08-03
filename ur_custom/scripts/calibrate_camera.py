#!/usr/bin/env python

import sys
import numpy as np
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

bridge = CvBridge()

class captureSend():
	def __init__(self):
		self.capture_image = rospy.ServiceProxy('capture_image', CaptureImage)
		self.group = moveit_commander.MoveGroupCommander("manipulator")
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
        			cv2.imwrite('calibration_images/checkerboard'+str(self.count)+'.jpeg', cv2_img)

       	 	except rospy.ServiceException, e:
        		print ("Service call failed: %s"%e)

	def move_robot(self):
		time.sleep(5)
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.5
		pose_goal.orientation.y = 0.5
		pose_goal.orientation.z = -0.5
		pose_goal.orientation.w = 0.5
		pose_goal.position.x = -0.50
		pose_goal.position.y = 0.0
		pose_goal.position.z = 0.7
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.291558964145
		pose_goal.orientation.y = 0.291057470962
		pose_goal.orientation.z = -0.644337178617
		pose_goal.orientation.w = 0.644289158123
		pose_goal.position.x = -0.550003824433
		pose_goal.position.y = 0.0410436404787
		pose_goal.position.z = 0.663785858288
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.605613239458
		pose_goal.orientation.y = 0.314254944388
		pose_goal.orientation.z = -0.653215458798
		pose_goal.orientation.w = 0.328307780152
		pose_goal.position.x = -0.518497985519
		pose_goal.position.y = 0.0334208906592
		pose_goal.position.z = 0.646199832625
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.481541011588
		pose_goal.orientation.y = 0.493296125559
		pose_goal.orientation.z = -0.530992374693
		pose_goal.orientation.w = 0.492772041299
		pose_goal.position.x = -0.515962875117
		pose_goal.position.y = 0.0170530677943
		pose_goal.position.z = 0.704129299506
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.665295824139
		pose_goal.orientation.y = 0.569565994532
		pose_goal.orientation.z = -0.334927430103
		pose_goal.orientation.w = 0.347562455999
		pose_goal.position.x = -0.559115992737
		pose_goal.position.y = -0.0521707920078
		pose_goal.position.z = 0.630004141186
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.637441729664
		pose_goal.orientation.y = 0.600720160124
		pose_goal.orientation.z = -0.350972489186
		pose_goal.orientation.w = 0.331091592068
		pose_goal.position.x = -0.562589356589
		pose_goal.position.y = -0.0549348779807
		pose_goal.position.z = 0.634726138665
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.494692899603
		pose_goal.orientation.y = 0.466016201817
		pose_goal.orientation.z = -0.533793658933
		pose_goal.orientation.w = 0.503162165122
		pose_goal.position.x = -0.559555909591
		pose_goal.position.y = -0.00464149569069
		pose_goal.position.z = 0.651925908999
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.535547257025
		pose_goal.orientation.y = 0.50469426486
		pose_goal.orientation.z = -0.492806308614
		pose_goal.orientation.w = 0.464343382312
		pose_goal.position.x = -0.558637172538
		pose_goal.position.y = 0.0121109409529
		pose_goal.position.z = 0.658053695701
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.orientation.x = 0.5
		pose_goal.orientation.y = 0.5
		pose_goal.orientation.z = -0.5
		pose_goal.orientation.w = 0.5
		pose_goal.position.x = -0.50
		pose_goal.position.y = 0.0
		pose_goal.position.z = 0.7
		self.group.set_pose_target(pose_goal)
		self.group.go(pose_goal, wait=True)
		self.group.stop()
		time.sleep(1)
		self.process()

	def calibrate_camera(self):
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		objp = np.zeros((8*6,3), np.float32)
		objp[:,:2] = np.mgrid[0:8,0:6].T.reshape(-1,2)
		objpoints = []
		imgpoints = [] 
		for i in range(1,10):
			img = cv2.imread('calibration_images/checkerboard'+str(i)+'.jpeg')
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			ret, corners = cv2.findChessboardCorners(gray, (8,6),None)
			if ret == True:
				objpoints.append(objp)
				corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
				imgpoints.append(corners2)
				img = cv2.drawChessboardCorners(img, (8,6), corners2,ret)
				cv2.imwrite('calibration_images_marked/checkerboard_corners'+str(i)+'.jpeg', img)
		ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

		for i in range(1,10):
	    		img = cv2.imread('calibration_images/checkerboard'+str(i)+'.jpeg')
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			ret, corners = cv2.findChessboardCorners(gray, (8,6),None)
	    		if ret == True:
				corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
				ret, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)

if __name__ == "__main__":
	moveit_commander.roscpp_initialize(sys.argv)	
	rospy.init_node("calibrate_camera")
	time.sleep(2)
	cs = captureSend()
	cs.move_robot()
	cs.calibrate_camera()
