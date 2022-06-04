from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
import launch_ros
from pathlib import Path
import launch


def generate_launch_description():
    base_path = os.path.realpath(get_package_share_directory("dummy_object_publisher"))
    config_path = (
        Path(base_path) / "configs" / "dummy_3d_publisher_config.json"
    ).as_posix()
    node = Node(
        package="dummy_object_publisher",
        executable="dummy_3d_publisher_node",
        name="dummy_3d_publisher_node",
        output="screen",
        emulate_tty=True,
        parameters=[
            {
             "dt": launch.substitutions.LaunchConfiguration("dt"),
             "config_file_path": launch.substitutions.LaunchConfiguration("config_file_path"),
             "target_frame":launch.substitutions.LaunchConfiguration("target_frame"),
             "use_sim_time": True
            },
            
        ],
    )


    return LaunchDescription(
        [
            launch.actions.DeclareLaunchArgument(
                name="dt", default_value="0.2"
            ),
            launch.actions.DeclareLaunchArgument(
                name="config_file_path", default_value=config_path
            ),
            launch.actions.DeclareLaunchArgument(
                name="target_frame", default_value="map"
            ),
            node
        ]
    )
