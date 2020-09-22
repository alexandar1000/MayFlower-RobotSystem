//
// Created by aunroel on 9/21/20.
//
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <tf2_ros/static_transform_broadcaster.h>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    ros::init(argc, argv, "tf_transforms");
    ros::NodeHandle n;

    vector<geometry_msgs::TransformStamped> transforms;

    tf2_ros::StaticTransformBroadcaster broadcaster;

    ros::Rate r(100);

    geometry_msgs::TransformStamped base_to_left;
    base_to_left.header.frame_id = "base_link";
    base_to_left.header.stamp = ros::Time::now();
    base_to_left.child_frame_id = "left_balancer";
    base_to_left.transform.translation.x = 0.7;
    base_to_left.transform.translation.y = 0.3;
    base_to_left.transform.translation.z = 0.0;
//    tf::Quaternion quaternion = tf::createQuaternionFromYaw(1);
//    tf::Quaternion quaternion(0,0,0,1);
    base_to_left.transform.rotation = tf::createQuaternionMsgFromRollPitchYaw(0,0,1);
//    base_to_left.transform.rotation.y = quaternion.y();
//    base_to_left.transform.rotation.z = quaternion.z();
//    base_to_left.transform.rotation.w = quaternion.w();

    geometry_msgs::TransformStamped base_to_right;
    base_to_right.header.frame_id = "base_link";
    base_to_right.header.stamp = ros::Time::now();
    base_to_right.child_frame_id = "right_balancer";
    base_to_right.transform.translation.x = 0.7;
    base_to_right.transform.translation.y = -0.3;
    base_to_right.transform.translation.z = 0.0;
    base_to_right.transform.rotation = tf::createQuaternionMsgFromRollPitchYaw(0,0,1);
//    base_to_left.transform.rotation.x = quaternion.x();
//    base_to_left.transform.rotation.y = quaternion.y();
//    base_to_left.transform.rotation.z = quaternion.z();
//    base_to_left.transform.rotation.w = quaternion.w();

    geometry_msgs::TransformStamped base_to_boat_rear;
    base_to_boat_rear.header.frame_id = "base_link";
    base_to_boat_rear.header.stamp = ros::Time::now();
    base_to_boat_rear.child_frame_id = "boat_rear";
    base_to_boat_rear.transform.translation.x = -0.8;
    base_to_boat_rear.transform.translation.y = 0.0;
    base_to_boat_rear.transform.translation.z = 0.0;
    base_to_boat_rear.transform.rotation = tf::createQuaternionMsgFromRollPitchYaw(0,0,1);
//    base_to_left.transform.rotation.x = quaternion.x();
//    base_to_left.transform.rotation.y = quaternion.y();
//    base_to_left.transform.rotation.z = quaternion.z();
//    base_to_left.transform.rotation.w = quaternion.w();

    geometry_msgs::TransformStamped base_to_video_camera;
    base_to_video_camera.header.frame_id = "base_link";
    base_to_video_camera.header.stamp = ros::Time::now();
    base_to_video_camera.child_frame_id = "video_camera";
    base_to_video_camera.transform.translation.x = 0.4;
    base_to_video_camera.transform.translation.y = 0.0;
    base_to_video_camera.transform.translation.z = 0.325;
    base_to_video_camera.transform.rotation = tf::createQuaternionMsgFromRollPitchYaw(0,0,1);

    //    base_to_left.transform.rotation.x = quaternion.x();
//    base_to_left.transform.rotation.y = quaternion.y();
//    base_to_left.transform.rotation.z = quaternion.z();
//    base_to_left.transform.rotation.w = quaternion.w();


    transforms.push_back(base_to_left);
    transforms.push_back(base_to_right);
    transforms.push_back(base_to_boat_rear);
    transforms.push_back(base_to_video_camera);

    while (n.ok()) {
        broadcaster.sendTransform(transforms);
        r.sleep();
    }
}
