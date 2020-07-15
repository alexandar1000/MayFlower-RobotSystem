# MayFlower-RobotSystem
### Branch zl_initalTesting
This is a running version for ROS - Unity connection: 
The host maching has Windows 10 system with Unity 2019.4.1f1 installed;
Ubuntu 20.04 with ROS1 noetic Virtual Machine is deployed on VirtualBox;
+ Following the ROS# Tutorial [Install Unity3D On Windows](https://github.com/siemens/ros-sharp/wiki/User_Inst_Unity3DOnWindows) to setup ROS # on Unity;
+ Copy the catkin_ws in this branch to the Ubuntu20.04 system;
+ Use "roslaunch rosbridge_server rosbridge_websocket.launch" to launch the rosbridge server;
+ Following [This Tutorial](https://www.youtube.com/watch?v=lVa_bb0UFMs) to create ROS connector gameObject on Unity;
+ Check the IP of the virtual machine and paste it to ROS Bridge Server Url on ROS Connector;
+ Add TestScript.cs and change the topic to "/chatter";
+ In the virtual machine, rosrun beginner_tutorials talker.py;
+ In Unity, click play to test the counter mounting.

**Note for setup the VirtualBox network:**
Enable three adapter: NAT, Host-only Adapter (Promiscuous mode: Allow VMs, Cable connected), Bridged Adapter (Intel Ethernet Connection; Promiscuous mode: Allow VMs, Cable connected).

