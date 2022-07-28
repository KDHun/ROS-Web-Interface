FROM nvidia/cudagl:11.1.1-base-ubuntu20.04

SHELL ["/bin/bash", "-c"]

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt update && apt install -y curl gnupg2 lsb-release
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt update
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y ros-foxy-desktop

RUN apt-get install python3-rosdep -y


RUN apt install python3-colcon-common-extensions -y

RUN apt-get update && apt-get install -y ros-foxy-gazebo-* 
RUN apt-get install -y ros-foxy-cartographer 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ros-foxy-cartographer-ros 
RUN apt-get install -y ros-foxy-navigation2 
RUN apt-get update && apt-get install -y ros-foxy-nav2-bringup

RUN source /opt/ros/foxy/setup.bash && apt-get install -y ros-foxy-dynamixel-sdk && \
    apt-get install -y ros-foxy-turtlebot3-msgs && \
    apt-get install -y ros-foxy-turtlebot3

RUN apt-get remove -y ros-foxy-turtlebot3-msgs
RUN apt-get remove -y ros-foxy-turtlebot3
RUN apt-get install -y git
WORKDIR /turtlebot3_ws/src

RUN git clone -b foxy-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git \
    && git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git && \
    git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3.git && \
    git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
WORKDIR /turtlebot3_ws

RUN source /opt/ros/foxy/setup.bash && colcon build --symlink-install

COPY ros2_entrypoint.sh /root/.
ENTRYPOINT ["/root/ros2_entrypoint.sh"]
CMD ["bash"]
