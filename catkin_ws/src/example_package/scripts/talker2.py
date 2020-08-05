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

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Pose

pose_msg = Pose()

boatPosition_x = 0
boatPosition_y = 0
boatPosition_z = 0

turn = 0

pose_msg.orientation.x = 0
pose_msg.orientation.y = 0
pose_msg.orientation.z = 0
pose_msg.orientation.w = 1

def talker():
    #pub = rospy.Publisher('data_topic', Float64, queue_size=10) # TOPIC
    pub = rospy.Publisher('chatter_', Pose, queue_size=10) # TOPIC
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    k=0.2
    
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % k
        variable = k
        #pub.publish(variable)
        
        boatPosition_x = rospy.get_param('boatPosition_x')
        boatPosition_y = rospy.get_param('boatPosition_y')
        boatPosition_z = rospy.get_param('boatPosition_z')
        
        frontCentreSensor = rospy.get_param('frontCentreSensor')
        frontRightSensor = rospy.get_param('frontRightSensor')
        frontRightAngleSensor = rospy.get_param('frontRightAngleSensor')
        frontLeftSensor = rospy.get_param('frontLeftSensor')
        frontLeftAngleSensor = rospy.get_param('frontLeftAngleSensor')
        
        if(frontRightSensor == 1):
            turn = -1
        elif(frontLeftSensor == 1):
            turn = 1
        elif(frontCentreSensor == 1):
            turn = 1
        elif(frontRightAngleSensor == 1):
            turn = -0.5
        elif(frontLeftAngleSensor == 1):
            turn = 0.5
        else:
            turn = 0
        
        #if(boatPosition_z > 20):
        #    turn = 1
        #elif(boatPosition_z < -20):
        #    turn = -1
        #else:
        #    turn = 0
        
        pose_msg.position.x = turn
        pose_msg.position.y = 0
        pose_msg.position.z = 0
        
        pub.publish(pose_msg)
        #rospy.loginfo('Envio: %s', variable)
        rospy.loginfo('SEND DATA: \n%s', pose_msg)
        k=k+0.1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass  
    
