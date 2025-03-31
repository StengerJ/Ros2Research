#!/bin/bash

export ROS_DOMAIN_ID=1312
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
source /opt/ros/humble/setup.bash
echo "Running Node A on $(hostname -I)"
echo "ROS_DOMAIN_ID set to $ROS_DOMAIN_ID"
python3 node1.py
