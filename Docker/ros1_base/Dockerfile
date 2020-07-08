FROM ros:noetic-ros-core-buster

# Setting default shell to bash
SHELL ["/bin/bash", "--login", "-c"]

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
   build-essential \
   python3-rosdep \
   python3-rosinstall \
   vim\
   && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
 rosdep update --rosdistro $ROS_DISTRO

# Create a workspace
RUN mkdir -p /home/catkin_ws/src

# Source the underlay workspace
RUN source /opt/ros/noetic/setup.bash && \
   cd  /home/catkin_ws && \
   echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc

# Initialise the overlay workspace
RUN cd  /home/catkin_ws && \
  catkin_make

WORKDIR /home