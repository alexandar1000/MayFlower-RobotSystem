#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from std_msgs.msg import String

# x = 0
# y = 0
# z = 0
message = ''

def control_callback(pose_message):
    # rospy.loginfo(rospy.get_caller_id() +
    #               f" I heard [{pose_message.position.x}, {pose_message.position.y}, {pose_message.position.z}]")
    rospy.loginfo(rospy.get_caller_id() + f" heard '{pose_message.data}' command")
    # global x, y, z

    global message
    # x = pose_message.position.x
    # y = pose_message.position.y
    # z = pose_message.position.z
    message = pose_message.data


def controller():
    rospy.init_node('unity_controls_node', anonymous=False)
    cmd_controls_topic = '/boat/controls'
    controls_publisher = rospy.Publisher(cmd_controls_topic, Pose, queue_size=10)

    teleop_topic = '/boat_teleop/cmd_vel'
    rospy.Subscriber(teleop_topic, String, control_callback)

    pose_msg = Pose()

    pose_msg.position.y = 0
    pose_msg.orientation.x = 0
    pose_msg.orientation.y = 0
    pose_msg.orientation.z = 0
    pose_msg.orientation.w = 1

    loop_rate = rospy.Rate(10)
    # global x, y, z
    global message

    try:
        while not rospy.is_shutdown():
            if message == '':
                continue

            rospy.loginfo(rospy.get_caller_id() + f' issuing command ["{message}"]')

            if message == 'w':
                pose_msg.position.x = 1
                pose_msg.position.z = 0
            elif message == 's':
                pose_msg.position.x = -1
                pose_msg.position.z = 0
            elif message == 'a':
                if pose_msg.position.z == 1:
                    pose_msg.position.z = 0
                else:
                    pose_msg.position.z = -1
                pose_msg.position.x = 0
            elif message == 'd':
                if pose_msg.position.z == -1:
                    pose_msg.position.z = 0
                else:
                    pose_msg.position.z = 1
                pose_msg.position.x = 0

            controls_publisher.publish(pose_msg)
            # pose_msg.position.z = 0
            # controls_publisher.publish(pose_msg)

            loop_rate.sleep()

            message = ''

    except Exception as e:
        print(e)

    finally:
        pose_msg = Pose()
        pose_msg.position.x = 0
        pose_msg.position.y = 0
        pose_msg.position.z = 0
        controls_publisher.publish(pose_msg)


    while not rospy.is_shutdown():
        # if x == 0 and z == 0:
        if message == '':
            continue
        else:
            # rospy.loginfo(rospy.get_caller_id() + f' issuing commands [{x}, {y}, {z}]')
            rospy.loginfo(rospy.get_caller_id() + f' issuing command ["{message}"]')

            if message == 'w':
                pose_msg.position.x = 1
            elif message == 's':
                pose_msg.position.x = -1
            elif message == 'a':
                pose_msg.position.z = -1
            elif message == 'd':
                pose_msg.position.z = 1
            # pose_msg.position.x = x
            # pose_msg.position.y = y
            # pose_msg.position.z = z

            controls_publisher.publish(pose_msg)
            # time.sleep(2)
            loop_rate.sleep()
            # x, z = 0, 0
            message = ''


if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInternalException:
        rospy.loginfo('node terminated')