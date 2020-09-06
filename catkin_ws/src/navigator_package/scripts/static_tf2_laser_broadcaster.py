#!/usr/bin/env python  
import rospy
import tf
import tf2_ros
import geometry_msgs.msg
import tf2_msgs.msg


class FixedLaserTransform:

	def __init__(self):
		self.pub_tf = rospy.Publisher('/tf', tf2_msgs.msg.TFMessage, queue_size=1)

		while not rospy.is_shutdown():
			# Run this loop at about 10 Hz
			rospy.sleep(0.1)

			t = geometry_msgs.msg.TransformStamped()
			t.header.frame_id = 'base_link'
			t.header.stamp = rospy.Time.now()
			t.child_frame_id = 'video_camera'
			t.transform.translation.x = 0.4
			t.transform.translation.y = 0.0
			t.transform.translation.z = 0.325

			t.transform.rotation.x = 0.0
			t.transform.rotation.y = 0.0
			t.transform.rotation.z = 0.0
			t.transform.rotation.w = 1.0

			tfm = tf2_msgs.msg.TFMessage([t])
			self.pub_tf.publish(tfm)


if __name__ == '__main__':
	try:
		rospy.init_node('fixed_laser_tf2_broadcaster')
		tfb = FixedLaserTransform()

		rospy.spin()
	except rospy.ROSInternalException:
		rospy.loginfo('static laser transform node terminated')
	# broadcaster = tf2_ros.StaticTransformBroadcaster()
	# static_transformStamped = geometry_msgs.msg.TransformStamped()
	# static_transformStamped.header.stamp = rospy.Time.now()
	# static_transformStamped.header.frame_id = "base_link"
	# static_transformStamped.child_frame_id = "laser_sensor_link"
	# static_transformStamped.transform.translation.x = 0.4
	# static_transformStamped.transform.translation.y = 0.5
	# static_transformStamped.transform.translation.z = 0.325
	# q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
	# static_transformStamped.transform.rotation.x = q[0]
	# static_transformStamped.transform.rotation.y = q[1]
	# static_transformStamped.transform.rotation.z = q[2]
	# static_transformStamped.transform.rotation.w = q[3]
	# broadcaster.sendTransform(static_transformStamped)
	# rospy.spin()