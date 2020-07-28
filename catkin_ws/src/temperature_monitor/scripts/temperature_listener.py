 #!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def temperature_update_handler(data):
    rospy.loginfo(rospy.get_caller_id() + 'The temperature is: %f', data.data)

def listener():
    rospy.init_node('temperature_listener', anonymous=False)

    rospy.Subscriber('temperature_reading', Float64, temperature_update_handler)

    # Start the node
    rospy.spin()

if __name__ == '__main__':
    listener()
