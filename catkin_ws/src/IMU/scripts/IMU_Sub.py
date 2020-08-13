import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3, Quaternion
from std_msgs.msg import Header, Float64

def callback(data):
    orientation = "Boat orientation: ({:.4f},{:.4f},{:.4f},{:.4f})" .format(data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w)
    header = "IMU Header frameID: " + data.header.frame_id
    angular_v = "Boat's angular velocity: roll {:.4f}, yaw {:.4f}, pitch {:.4f}.".format(data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z)
    linear_a = "Boat's linear acceleration: forward {:.4f}, up {:.4f}, left{:.4f}." .format(data.linear_acceleration.z, data.linear_acceleration.y, data.linear_acceleration.x)  
    rospy.loginfo(rospy.get_caller_id() +"\n" + header + "\n" + orientation + "\n" +angular_v + "\n" + linear_a)
    # Set battery power as ros parameter
    rospy.set_param('imu_orient', orientation);
    rospy.set_param('imu_angularVel_roll', data.angular_velocity.x);
    rospy.set_param('imu_angularVel_yaw', data.angular_velocity.y);
    rospy.set_param('imu_angularVel_pitch', data.angular_velocity.z);
    rospy.set_param('imu_linearAccel_forward', data.linear_acceleration.z);
    rospy.set_param('imu_linearAccel_up', data.linear_acceleration.y);
    rospy.set_param('imu_linearAccel_left', data.linear_acceleration.x);
    

def subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('imuSubscriber', anonymous=True)

    rospy.Subscriber('imuData', Imu, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
