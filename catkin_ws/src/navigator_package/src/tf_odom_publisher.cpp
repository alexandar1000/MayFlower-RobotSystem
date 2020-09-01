#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "odometry_publisher");

  ros::NodeHandle n;
  tf::TransformBroadcaster odom_broadcaster;


  ros::Time current_time, last_time;
  current_time = ros::Time::now();
  last_time = ros::Time::now();

  ros::Rate r(1.0);
  while(n.ok()){

    ros::spinOnce();               // check for incoming messages
    current_time = ros::Time::now();

    //first, we'll publish the transform over tf
    geometry_msgs::TransformStamped odom_trans;
    odom_trans.header.stamp = current_time;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_link";

    odom_trans.transform.translation.x = x;
    odom_trans.transform.translation.y = y;
    odom_trans.transform.translation.z = 0.0;
    odom_trans.transform.rotation = odom_quat;

    odom_trans.transform.rotation.x = odom.pose.pose.orientation.x;
  	odom_trans.transform.rotation.y = odom.pose.pose.orientation.y;
  	odom_trans.transform.rotation.z = odom.pose.pose.orientation.z;
  	odom_trans.transform.rotation.w = odom.pose.pose.orientation.w;

    //send the transform
    odom_broadcaster.sendTransform(odom_trans);


    last_time = current_time;
    r.sleep();
  }
}
