#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg
from nav_msgs.msg import Odometry


def handle_odom(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "odom"
    t.child_frame_id = "base_link"
    t.transform.translation.x = msg.pose.pose.position.x
    t.transform.translation.y = msg.pose.pose.position.y
    t.transform.translation.z = 0.0
    t.transform.rotation.x = msg.pose.pose.orientation.x
    t.transform.rotation.y = msg.pose.pose.orientation.y
    t.transform.rotation.z = msg.pose.pose.orientation.z
    t.transform.rotation.w = msg.pose.pose.orientation.w

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_odom_broadcaster')
    rospy.Subscriber("/odom",
                     Odometry,
                     handle_odom,
                     )
    rospy.spin()