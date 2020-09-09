#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose


x = 0
y = 0
z = 0


def control_callback(pose_message):
    rospy.loginfo(rospy.get_caller_id() +
                  f" I heard [{pose_message.position.x}, {pose_message.position.y}, {pose_message.position.z}]")
    global x, y, z
    x = pose_message.position.x
    y = pose_message.position.y
    z = pose_message.position.z


def controller():
    rospy.init_node('unity_controls_node', anonymous=False)
    cmd_controls_topic = '/unity/controls'
    controls_publisher = rospy.Publisher(cmd_controls_topic, Pose, queue_size=10)

    teleop_topic = '/boat_teleop/cmd_vel'
    rospy.Subscriber(teleop_topic, Pose, control_callback)

    pose_msg = Pose()

    pose_msg.orientation.x = 0
    pose_msg.orientation.y = 0
    pose_msg.orientation.z = 0
    pose_msg.orientation.w = 1

    loop_rate = rospy.Rate(10)
    global x, y, z

    while not rospy.is_shutdown():
        if x == 0 and z == 0:
            continue
        else:
            rospy.loginfo(rospy.get_caller_id() + f' issuing commands [{x}, {y}, {z}]')
            pose_msg.position.x = x
            pose_msg.position.y = y
            pose_msg.position.z = z

            controls_publisher.publish(pose_msg)
            # time.sleep(2)
            loop_rate.sleep()
            x, z = 0, 0


if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInternalException:
        rospy.loginfo('node terminated')