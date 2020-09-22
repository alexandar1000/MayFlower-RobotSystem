#!/usr/bin/env python
import rospy

import tf_conversions

import tf2_ros
import geometry_msgs.msg
import nav_msgs.msg


def handle_boat_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'odom'
    t.child_frame_id = 'base_link'
    t.transform.translation.x = msg.pose.pose.position.x
    t.transform.translation.y = msg.pose.pose.position.y
    t.transform.translation.z = 0.0
    t.transform.rotation = msg.pose.pose.orientation
    # q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.pose.pose.orientation.z)
    # t.transform.rotation.x = q[0]
    # t.transform.rotation.y = q[1]
    # t.transform.rotation.z = q[2]
    # t.transform.rotation.w = q[3]

    br.sendTransform(t)


if __name__ == '__main__':
    rospy.init_node('tf2_boat_broadcaster')
    rospy.Subscriber('/odom', nav_msgs.msg.Odometry, handle_boat_pose, queue_size=1)
    rospy.spin()
