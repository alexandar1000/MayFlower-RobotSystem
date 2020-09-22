#include <ros/ros.h>
#include <geometry_msgs/PointStamped.h>
#include <tf/transform_listener.h>

geometry_msgs::PoseStamped base_link;

void poseCallback(const geometry_msgs::PoseStamped::ConstPtr& point) {
    base_link.header.frame_id = point->header.frame_id;
    base_link.header.stamp = point->header.stamp;
    base_link.pose.position.x = point->pose.position.x;
    base_link.pose.position.y = point->pose.position.y;
    base_link.pose.position.z = 0.0;

    base_link.pose.orientation.x = point->pose.orientation.x;
    base_link.pose.orientation.y = point->pose.orientation.y;
    base_link.pose.orientation.z = point->pose.orientation.z;
    base_link.pose.orientation.w = point->pose.orientation.w;
}

void transformLeft(const tf::TransformListener& listener) {
    try {
        geometry_msgs::PoseStamped left_balancer;
        listener.transformPose("left_balancer", base_link, left_balancer);
        ROS_INFO("base_link.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] ----> "
                 "left_balancer.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] at time %.2f",
                    base_link.pose.position.x, base_link.pose.position.y, base_link.pose.position.z,
                    base_link.pose.orientation.x, base_link.pose.orientation.y, base_link.pose.orientation.z,
                    base_link.pose.orientation.w, left_balancer.pose.position.x, left_balancer.pose.position.y,
                 left_balancer.pose.position.z, left_balancer.pose.orientation.x, left_balancer.pose.orientation.y,
                 left_balancer.pose.orientation.z, left_balancer.pose.orientation.w,left_balancer.header.stamp.toSec());
    } catch (tf::TransformException& ex) {
        ROS_ERROR("Received an exception trying to transform a point from \"base_link\" to \"left_balancer\": %s", ex.what());
    }
}

void transformRight(const tf::TransformListener& listener) {
    try{
        geometry_msgs::PoseStamped right_balancer;
        listener.transformPose("right_balancer", base_link, right_balancer);
        ROS_INFO("base_link.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] ----> "
             "right_balancer.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] at time %.2f",
             base_link.pose.position.x, base_link.pose.position.y, base_link.pose.position.z,
             base_link.pose.orientation.x, base_link.pose.orientation.y, base_link.pose.orientation.z,
             base_link.pose.orientation.w, right_balancer.pose.position.x, right_balancer.pose.position.y,
             right_balancer.pose.position.z, right_balancer.pose.orientation.x, right_balancer.pose.orientation.y,
             right_balancer.pose.orientation.z, right_balancer.pose.orientation.w,right_balancer.header.stamp.toSec());
    } catch (tf::TransformException& ex) {
    ROS_ERROR("Received an exception trying to transform a point from \"base_link\" to \"right_balancer\": %s",
              ex.what());
    }
}

void transformRear(const tf::TransformListener& listener) {
    try{
        geometry_msgs::PoseStamped boat_rear;
        listener.transformPose("boat_rear", base_link, boat_rear);
        ROS_INFO("base_link.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] ----> "
                 "boat_rear.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] at time %.2f",
                 base_link.pose.position.x, base_link.pose.position.y, base_link.pose.position.z,
                 base_link.pose.orientation.x, base_link.pose.orientation.y, base_link.pose.orientation.z,
                 base_link.pose.orientation.w, boat_rear.pose.position.x, boat_rear.pose.position.y,
                 boat_rear.pose.position.z, boat_rear.pose.orientation.x, boat_rear.pose.orientation.y,
                 boat_rear.pose.orientation.z, boat_rear.pose.orientation.w,boat_rear.header.stamp.toSec());
    } catch (tf::TransformException& ex) {
        ROS_ERROR("Received an exception trying to transform a point from \"base_link\" to \"right_balancer\": %s",
                  ex.what());
    }
}
void transformCamera(const tf::TransformListener& listener) {
    try{
        geometry_msgs::PoseStamped video_camera;
        listener.transformPose("video_camera", base_link, video_camera);
        ROS_INFO("base_link.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] ----> "
                 "video_camera.position[%.2f, %.2f, %.2f].orientation[%.2f, %.2f, %.2f, %.2f] at time %.2f",
                 base_link.pose.position.x, base_link.pose.position.y, base_link.pose.position.z,
                 base_link.pose.orientation.x, base_link.pose.orientation.y, base_link.pose.orientation.z,
                 base_link.pose.orientation.w, video_camera.pose.position.x, video_camera.pose.position.y,
                 video_camera.pose.position.z, video_camera.pose.orientation.x, video_camera.pose.orientation.y,
                 video_camera.pose.orientation.z, video_camera.pose.orientation.w,video_camera.header.stamp.toSec());
    } catch (tf::TransformException& ex) {
        ROS_ERROR("Received an exception trying to transform a point from \"base_link\" to \"right_balancer\": %s",
                  ex.what());
    }
}


int main(int argc, char** argv) {
    ros::init(argc, argv, "robot_tf_listener");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("boat_pose", 1000, poseCallback);

    tf::TransformListener listener(ros::Duration(10));

    ros::Timer left = n.createTimer(ros::Duration(0.1), boost::bind(&transformLeft, boost::ref(listener)));
    ros::Timer right = n.createTimer(ros::Duration(0.1), boost::bind(&transformRight, boost::ref(listener)));
    ros::Timer rear = n.createTimer(ros::Duration(0.1), boost::bind(&transformRear, boost::ref(listener)));
    ros::Timer camera = n.createTimer(ros::Duration(0.1), boost::bind(&transformCamera, boost::ref(listener)));

    ros::spin();
}
