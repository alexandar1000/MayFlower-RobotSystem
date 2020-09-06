//#include <ros/ros.h>
//#include <geometry_msgs/PointStamped.h>
//#include <tf/transform_listener.h>
//
//int base_x = 0;
//int base_y = 0;
//int base_z = 0;
//
//void basePoseCallback(const geometry_msgs::PoseStamped& msg) {
//    base_x = msg.pose.position.x;
//    base_y = msg.pose.position.y;
//    base_z = msg.pose.position.z;
//}
//
//void transformBaseToBoatRear(const tf::TransformListener& listener) {
//    geometry_msgs::PointStamped base_point;
//    boat_rear.header.frame_id = "boat_rear";
//
//    boat_rear.header.stamp = ros::Time();
//
//    boat_rear.point.x = 0;
//    boat_rear.point.y = 0;
//    boat_rear.point.z = 0;
//
//    try {
//        geometry_msgs::PointStamped boat_rear;
//        listener.transformPoint("boat_rear", base_point, boat_rear);
//
//        ROS_INFO("boat_rear: (%.2f, %.2f. %.2f) -----> base_link: (%.2f, %.2f, %.2f) at time %.2f",
//                 boat_rear.point.x, boat_rear.point.y, boat_rear.point.z,
//                 base_point.point.x, base_point.point.y, base_point.point.z, base_point.header.stamp.toSec());
//    }
//    catch(tf::TransformException& ex){
//        ROS_ERROR("Received an exception trying to transform a point from \"boat_rear\" to \"base_link\": %s", ex.what());
//    }
//}
//
//int main(int argc, char** argv) {
//    ros::init(argc, argv, "boat_rear_tf_listener");
//    ros::NodeHandle transform_node;
//    ros::NodeHandle base_listener;
//    ros::Subscriber base_sub = base_listener.subscribe('pose', 100, basePoseCallback);
//    tf::TransformListener listener(ros::Duration(10));
//
//    ros::Timer timer = transform_node.createTimer(ros::Duration(0.5), boost::bind(&transformBoatRear, boost::ref(listener)));
//
//    ros::spin();
//}