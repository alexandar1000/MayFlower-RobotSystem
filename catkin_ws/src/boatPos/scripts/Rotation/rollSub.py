import rospy
from std_msgs.msg import Float64

def callback(data):
    if(data.data > 0):
    	rospy.loginfo(rospy.get_caller_id() + 'Roll angle is: %.3f to the right.', data.data)
    else:
    	rospy.loginfo(rospy.get_caller_id() + 'Pitch angle is: %.3f to the left.', (-1) * data.data)
    
    # Set battery power as ros parameter
    rospy.set_param('roll_angle', round(data.data, 3))

def subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber('rollAngle', Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
