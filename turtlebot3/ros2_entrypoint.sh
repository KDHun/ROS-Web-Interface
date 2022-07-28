#!/bin/bash
set -e

source /opt/ros/foxy/setup.bash
source /turtlebot3_ws/install/setup.bash

/bin/bash -c 'TURTLEBOT3_MODEL=burger ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py &'  >> /dev/null
/bin/bash -c 'TURTLEBOT3_MODEL=burger ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True &' >> /dev/null
exec "$@"