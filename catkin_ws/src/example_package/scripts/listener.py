#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    
    if(data.data == 1):
    	rospy.set_param('frontCentreSensor', 1)
    	resetSensors(1)
    if(data.data == 2):
    	rospy.set_param('frontRightSensor', 1)
    	resetSensors(2)
    if(data.data == 3):
    	rospy.set_param('frontRightAngleSensor', 1)
    	resetSensors(3)
    if(data.data == 4):
    	rospy.set_param('frontLeftSensor', 1)
    	resetSensors(4)
    if(data.data == 5):
    	rospy.set_param('frontLeftAngleSensor', 1)
    	resetSensors(5)
    if(data.data == 6):
    	rospy.set_param('backSensor', 1)
    	resetSensors(6)
    
    
def resetSensors(sensor):
    if(sensor == 1):
	    rospy.set_param('frontRightSensor', 0)
	    rospy.set_param('frontRightAngleSensor', 0)
	    rospy.set_param('frontLeftSensor', 0)
	    rospy.set_param('frontLeftAngleSensor', 0)
	    rospy.set_param('backSensor', 0)
    if(sensor == 2):
	    rospy.set_param('frontCentreSensor', 0)
	    rospy.set_param('frontRightAngleSensor', 0)
	    rospy.set_param('frontLeftSensor', 0)
	    rospy.set_param('frontLeftAngleSensor', 0)
	    rospy.set_param('backSensor', 0)
    if(sensor == 3):
	    rospy.set_param('frontCentreSensor', 0)
	    rospy.set_param('frontRightSensor', 0)
	    rospy.set_param('frontLeftSensor', 0)
	    rospy.set_param('frontLeftAngleSensor', 0)
	    rospy.set_param('backSensor', 0)
    if(sensor == 4):
	    rospy.set_param('frontCentreSensor', 0)
	    rospy.set_param('frontRightSensor', 0)
	    rospy.set_param('frontRightAngleSensor', 0)
	    rospy.set_param('frontLeftAngleSensor', 0)
	    rospy.set_param('backSensor', 0)
    if(sensor == 5):
	    rospy.set_param('frontCentreSensor', 0)
	    rospy.set_param('frontRightSensor', 0)
	    rospy.set_param('frontRightAngleSensor', 0)
	    rospy.set_param('frontLeftSensor', 0)
	    rospy.set_param('backSensor', 0)  
    if(sensor == 6):
	    rospy.set_param('frontCentreSensor', 0)
	    rospy.set_param('frontRightSensor', 0)
	    rospy.set_param('frontRightAngleSensor', 0)
	    rospy.set_param('frontLeftSensor', 0)
	    rospy.set_param('frontLeftAngleSensor', 0) 

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('lasersensor_', Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
