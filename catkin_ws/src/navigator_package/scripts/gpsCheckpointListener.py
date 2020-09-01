#!/usr/bin/env python

import rospy
import message_filters
import json
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
from math import *

boat_lat = 0
boat_lon = 0
boat_alt = 0

beacon_dict= dict()
def beacon_callback(beacon_msg):
    global beacon_dict
    beacon_dict =json.load(beacon_msg)

def boat_callback(boat_data):
    global boat_lat, boat_alt, boat_lon
    boat_lat = data.latitude
    boat_lon = data.longitude
    boat_alt = data.altitude

def calc_distance():
    global boat_lat, boat_lon, boat_alt, beacon_dict


    gps_checkpoint_lat = beacon_dict["x"]
    gps_checkpoint_lon = beacon_dict["y"]


    delta_lat = (gps_checkpoint_lat*(108000) - boat_lat*(108000))
    delta_lon = (gps_checkpoint_lon*(108000) - boat_lon*(108000))

    hyp_m = (delta_lat**2 + delta_lon**2)**0.5
    hyp_ft = (hyp_m*3.2800839)
    rospy.loginfo("Distance is %s in ft.", hyp_ft)
    return hyp_ft

def get_angle():
    global boat_lat, boat_lon, beacon_dict
    return degrees(atan((boat_lat - beacon_dict['x']) / (boat_lon - beacon_dict['y'])))


def distanceTalker():
    rospy.init_node('gps_monitor', anonymous=True)
    beacon_topic = "beacon_gpsCheckpoint"
    rospy.Subscriber(beacon_topic, String, beacon_callback)
    boat_topic= "GPSSensor"
    rospy.Subscriber(boat_topic, NavSatFix, boat_callback)

    distance_topic= "GPS_Distance"
    distance_publisher=rospy.Publisher(distance_topic, String, queue_size=10)
    loop_rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        result = {
            'distance': calc_distance(),
            'angle': get_angle()
        }
        rospy.loginfo(rospy.get_caller_id() + f" distance = {result['distance']}, angle = {result['angle']}")
        distance_publisher.publish(json.dumps(result))
        loop_rate.sleep()


if __name__ == '__main__':
    try:
        distance_talker()
    except rospy.ROSInternalException:
        rospy.loginfo('node terminated')
