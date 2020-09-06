#!/usr/bin/env python
# to get commandline arguments
import sys

import rospy
import tf2_ros
import geometry_msgs.msg
import tf_conversions


if __name__ == '__main__':
    namespace = sys.argv[1]
    name = rospy.get_param(f'{namespace}/title')
    parent = rospy.get_param(f'{namespace}/parent')
    child = rospy.get_param(f'{namespace}/child')
    x = rospy.get_param(f'{namespace}/x_conv')
    y = rospy.get_param(f'{namespace}/y_conv')
    z = rospy.get_param(f'{namespace}/z_conv')

    rospy.init_node(f'{name}_tf2_broadcaster')

    broadcaster = tf2_ros.StaticTransformBroadcaster()
    static_transformStamped = geometry_msgs.msg.TransformStamped()
    static_transformStamped.header.stamp = rospy.Time.now()
    static_transformStamped.header.frame_id = parent
    static_transformStamped.child_frame_id = child
    static_transformStamped.transform.translation.x = x
    static_transformStamped.transform.translation.y = y
    static_transformStamped.transform.translation.z = z
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
    static_transformStamped.transform.rotation.x = q[0]
    static_transformStamped.transform.rotation.y = q[1]
    static_transformStamped.transform.rotation.z = q[2]
    static_transformStamped.transform.rotation.w = q[3]
    broadcaster.sendTransform(static_transformStamped)

    rospy.spin()
