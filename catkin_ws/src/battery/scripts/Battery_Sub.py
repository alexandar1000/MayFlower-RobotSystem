import rospy
from sensor_msgs.msg import BatteryState

def callback(data):
    status = ""
    if(data.power_supply_status == 0):
        status = "UNKNOWN"
    elif(data.power_supply_status == 1):
        status = "CHARGING"
    elif(data.power_supply_status == 2):
        status = "DISCHARGING"
    elif(data.power_supply_status == 3):
        status = "NOT_CHARGING"
    elif(data.power_supply_status == 4):
        status = "FULL"


    rospy.loginfo(rospy.get_caller_id() + 'Header stamp secs: {}, remaining power is: {}, status: {}'.format(data.header.stamp.secs, data.percentage, status))


    # Set battery power as ros parameter
    rospy.set_param('battery_percentage', data.percentage)
    rospy.set_param('battery_status', status)

def subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('batterySub', anonymous=True)

    rospy.Subscriber('battery', BatteryState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
