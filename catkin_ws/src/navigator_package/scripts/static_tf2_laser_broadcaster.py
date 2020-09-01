#!/usr/bin/env python  
import rospy
import tf
import tf2_ros
import math
import sys
import geometry_msgs.msg
import tf_conversions

if __name__ == '__main__':
	rospy.init_node('my_static_tf2_broadcaster')
	broadcaster = tf2_ros.StaticTransformBroadcaster()
	static_transformStamped = geometry_msgs.msg.TransformStamped()
	static_transformStamped.header.stamp = rospy.Time.now()
	static_transformStamped.header.frame_id = "base_link"
	static_transformStamped.child_frame_id = "base_laser"
	static_transformStamped.transform.translation.x = 3.14
	static_transformStamped.transform.translation.y = 0.0
	static_transformStamped.transform.translation.z = 0.0
	q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
	static_transformStamped.transform.rotation.x = q[0]
	static_transformStamped.transform.rotation.y = q[1]
	static_transformStamped.transform.rotation.z = q[2]
	static_transformStamped.transform.rotation.w = q[3]
	broadcaster.sendTransform(static_transformStamped)
	rospy.spin()