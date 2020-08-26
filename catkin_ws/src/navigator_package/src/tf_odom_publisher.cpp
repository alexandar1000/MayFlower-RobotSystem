#include <string>
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

tf::Transform transform;
tf::Quaternion q;

void odom_callback(const nav_msgs::Odometry &odom)
{
	ros::Time current_time;
	ros::Time last_time;
	current_time = ros::Time::now();
	last_time = ros::Time::now();

	tf::TransformBroadcaster broadcaster;

	geometry_msgs::TransformStamped odom_trans;
	odom_trans.header.frame_id = "odom";
	odom_trans.child_frame_id = "base_link";

  odom_trans.header.stamp = current_time;
  odom_trans.transform.translation.x = odom.pose.pose.position.x;
  odom_trans.transform.translation.y = odom.pose.pose.position.y;
  odom_trans.transform.translation.z = odom.pose.pose.position.z;
  odom_trans.transform.rotation.x = odom.pose.pose.orientation.x;
  odom_trans.transform.rotation.y = odom.pose.pose.orientation.y;
  odom_trans.transform.rotation.z = odom.pose.pose.orientation.z;
  odom_trans.transform.rotation.w = odom.pose.pose.orientation.w;


  last_time = current_time;
  // publishing the odometry and the new tf
  broadcaster.sendTransform(odom_trans);
}


int main(int argc, char** argv) {

	ros::init(argc, argv, "state_publisher");
	ros::NodeHandle n;
  ros::Subscriber odo_sub = n.subscribe("/odom", 1, odom_callback);
  ros::Rate loop_rate(100);

	while (ros::ok()) {
    ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}
