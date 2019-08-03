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
                self.cap = rospy.Service('capture_image', CaptureImage, self.capture)
		self.capture = 0
		self.img = Image()
		
	def callback(self, msg):
		if self.capture == 1:
                	try:
        			cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    			except CvBridgeError, e:
        			print(e)
    			else: 
				self.capture = 0 
				self.img = msg
 
        def capture(self, req):
		print('Image Captured')
		self.capture = req.capture
		return CaptureImageResponse(image = self.img)
                
if __name__ == "__main__":	
	rospy.init_node("capture_image_ur")
	sI = saveImage()
        rospy.spin()
