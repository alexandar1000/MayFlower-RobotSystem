import rospy
from std_msgs.msg import Float64

def testPublisher():
   pub = rospy.Publisher('batteryPower', Float64, queue_size=10) 
   rospy.init_node('testPublisher', anonymous=True)
   rate = rospy.Rate(1) # 10hz
   while not rospy.is_shutdown():
       data = 100 + rospy.get_time()
       rospy.loginfo(data)
       pub.publish(data)
       rate.sleep()

if __name__ == '__main__':
   try:
       testPublisher()
   except rospy.ROSInterruptException:
       pass
