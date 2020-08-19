import rospy
from sensor_msgs.msg import NavSatFix

def callback(data):
    lat = ""
    lon = ""
    alt = str(data.altitude) + "m"
    if data.latitude > 0:
    	lat = str(data.latitude) + " N"
    elif data.latitude < 0:
        lat = str(data.latitude * (-1)) + " S"
        
    if data.longitude > 0:
        lon = str(data.longitude) + " E"
    elif data.longitude < 0:
        lon = str(data.longitude * (-1)) + " W"
    
    rospy.loginfo(rospy.get_caller_id() +"Current GPS is ({0},{1},{2})".format(lat, lon, alt))
    
    # Set battery power as ros parameter
    rospy.set_param('gps_lat', data.latitude)
    rospy.set_param('gps_lon', data.longitude)
    rospy.set_param('gps_alt', data.altitude)
    

def subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('gpsSubscriber', anonymous=True)

    rospy.Subscriber('gpsData', NavSatFix, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
