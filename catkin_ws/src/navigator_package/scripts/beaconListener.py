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
import json
from math import *

from std_msgs.msg import String

beacon_dict = dict()
currentBeacon = 0

def converter(beacon_msg):
    beacon_dict = json.loads(beacon_msg)
    return beacon_dict['Items']

def getDegree(beacon):
    global boatX, boatZ
    dx = beacon['location']['x'] - boatX
    dz = beacon['location']['z'] - boatZ
    deg = degrees(atan2(dz, -dx))
    if(deg < 0):
        deg += 360
    return deg
    
def getDistance(beacon):
    global boatX, boatZ
    dx = beacon['location']['x'] - boatX
    dz = beacon['location']['z'] - boatZ
    return sqrt(dz**2 + dx**2)

def listener():

    rospy.init_node('beaconListener', anonymous=True)

    rospy.Subscriber('/beacons_', String, callback) #TOPIC

    rospy.spin()

def callback(data):
    global boatX, boatZ, currentBeacon
    boatX = rospy.get_param('boatPosition_x')
    boatZ = rospy.get_param('boatPosition_z')
    msg = (data.data).encode("utf-8").decode("unicode-escape")
    beaconsObj = converter(msg)
    deg = getDegree(beaconsObj[currentBeacon])
    dist = getDistance(beaconsObj[currentBeacon])
    
    if(dist < 5):
        currentBeacon += 1
    
    rospy.set_param('goalDirection', deg) 
    rospy.loginfo('Beacon direction: %s', deg)
    rospy.loginfo('Beacon distance: %s', dist)

if __name__ == '__main__':
    listener()
