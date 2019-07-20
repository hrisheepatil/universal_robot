#!/usr/bin/env python

import copy
import rospy
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from ur_custom.srv import CaptureImageResponse
from ur_custom.srv import CaptureImageRequest
from ur_custom.srv import CaptureImage
import cv2

bridge = CvBridge()

class saveImage:
	def __init__(self):
		self.image = rospy.Subscriber('/ur/camera1/image_raw', Image, self.callback)
                self.capture = rospy.Service('capture_image', CaptureImage, self.capture)
		self.capture = 0
		self.done = 0

	def callback(self, msg):
		if self.capture == 1:
                	try:
        			cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    			except CvBridgeError, e:
        			print(e)
    			else: 
        			time = msg.header.stamp
        			cv2.imwrite(''+str(time)+'.jpeg', cv2_img)
        			rospy.sleep(1)
			self.done = 2
			self.capture = 0 
 
        def capture(self, req):
		print('Image Captured')
		self.capture = req.capture
		if self.done == 2:
			req.done = 2
			self.done = 0
			return CaptureImageResponse(req.done)
                

if __name__ == "__main__":	
	rospy.init_node("capture_image")
	sI = saveImage()
        rospy.spin()
