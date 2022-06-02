# Copyright 2022 Siddharth Saha

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    config = os.path.join(get_package_share_directory("lgsvl_interface"), "param", "lgsvl_interface.param.yaml")
    return LaunchDescription(
        [
            Node(
                package="lgsvl_interface",
                executable="lgsvl_interface_node",
                name="lgsvl_interface_node",
                output="screen",
                parameters=[config],
                remappings=[
                    ("canbus", "/canbus"),
                    ("odometry", "/ego_racecar/odom")
                ],
            ),
        ]
    )