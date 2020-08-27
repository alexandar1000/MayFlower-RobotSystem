#!/usr/bin/env python
import sys
import termios
import tty
import os
import rospy
import fcntl
from geometry_msgs.msg import Pose


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# button_delay = 0.2



def cmd_receiver():
    rospy.init_node('unity_cmd_controls_node', anonymous=True)
    teleop_topic = '/remote/commands'
    pub = rospy.Publisher(teleop_topic, Pose, queue_size=10)
    loop_rate = rospy.Rate(10)
    x, y, z = -1, -1, -1

    pose = Pose()
    pose.orientation.x = 0
    pose.orientation.y = 0
    pose.orientation.z = 0
    pose.orientation.w = 1

    fd = sys.stdin.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    while not rospy.is_shutdown():


        char = getch()
        # if char == "p":
        #     print("Stop!")
        #     exit(0)

        if not char:
            x, y, z = -1, -1, -1

        elif char == "w":
            x = 1
        # time.sleep(button_delay)

        elif char == "a":
            z = -1
        # time.sleep(button_delay)

        elif char == "s":
            x = -1
        # time.sleep(button_delay)

        elif char == "d":
            z = 1
            # time.sleep(button_delay)

        if x != -1 or z != -1:
            rospy.loginfo(rospy.get_caller_id() + f' issuing commands [{x}, {y}, {z}]')
            pose.position.x = x
            pose.position.y = y
            pose.position.z = z
            pub.publish()
            x = -1
            z = -1

        loop_rate.sleep()


if __name__ == '__main__':
    try:
        cmd_receiver()
    except rospy.ROSInternalException:
        rospy.loginfo('node terminated')