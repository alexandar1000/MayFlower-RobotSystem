import rospy
from tf import broadcaster

def transformer():
    rospy.init_node('robot_tf_publisher')

    loop_rate = rospy.Rate(100)

    tf = broadcaster.TransformBroadcaster()

    while not rospy.is_shutdown():
        tf.sendTransformMessage(
            tf.sendTransform(tf.)
        )