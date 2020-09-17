#!/usr/bin/env python

# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import rospy
from geometry_msgs.msg import Pose
from std_msgs.msg import String
import sys
import select
import termios
import tty

msg = """
Control Your Boat!
---------------------------
Moving around:
        w    
   a    s    d

space key: force stop
anything else : stop smoothly
CTRL-C to quit
"""

moveBindings = {
    # 'w': (1, 0),
    # 'a': (0, -1),
    # 'd': (0, 1),
    # 's': (-1, 0)
    'w': 'w',
    'a': 'a',
    'd': 'd',
    's': 's'
}


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('boat_teleop')
    pub = rospy.Publisher('~cmd_vel', String, queue_size=5)

    # x = 0
    # z = 0
    message = ''
    count = 0
    try:
        while True:
            key = getKey()
            if key in moveBindings.keys():
                # x = moveBindings[key][0]
                # z = moveBindings[key][1]
                message = moveBindings[key]
                count = 0

            elif key == ' ':
                # x = 0
                # z = 0
                message = ''
            else:
                count = count + 1
                if count > 4:
                    # x = 0
                    # z = 0
                    message = ''
                if key == '\x03':
                    break

            # pose = Pose()
            # pose.position.x = x
            # pose.position.y = 0
            # pose.position.z = z

            # if x == 0 and z == 0:
            if message == '':
                continue
            else:
                pub.publish(message)
                # x = 0
                # z = 0
                message = ''

    except Exception as e:
        print(e)

    finally:
        # pose = Pose()
        # pose.position.x = 0
        # pose.position.y = 0
        # pose.position.z = 0
        # pub.publish(pose)
        pub.publish('')

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
