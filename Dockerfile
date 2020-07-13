FROM ros:noetic-ros-core-buster

# Setting default shell to bash
SHELL ["/bin/bash", "--login", "-c"]

# Install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
   build-essential \
   python3-rosdep \
   python3-rosinstall \
   ros-noetic-rosauth \
   vim \
   && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y\
   ros-noetic-rosauth \
   ros-noetic-rosbridge-server \
   && rm -rf /var/lib/apt/lists/*

RUN apt-get remove ros-noetic-rosbridge-server -y

# Bootstrap rosdep
RUN rosdep init && \
 rosdep update --rosdistro $ROS_DISTRO

# Source the underlay and overlay workspaces
RUN source /opt/ros/noetic/setup.bash && \
   echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc && \
   echo 'source /home/catkin_ws/devel/setup.bash' >> ~/.bashrc

WORKDIR /home

# Initialise a workspace
RUN mkdir -p /home/catkin_ws/src

# Copy the packages from the repository
COPY catkin_ws/src catkin_ws/src/

# Copy the convenience scripts
COPY aux/bootstrap.sh .
COPY aux/run_rosbridge.sh .

# Make the project
RUN cd catkin_ws && \
 catkin_make

EXPOSE 9090