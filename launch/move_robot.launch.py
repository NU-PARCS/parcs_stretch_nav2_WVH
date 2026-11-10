from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    stretch_core_path = get_package_share_directory('stretch_core')

    # Stretch driver in position mode (required for move_to_pose)
    stretch_driver_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([stretch_core_path, '/launch/stretch_driver.launch.py']),
        launch_arguments={'mode': 'position', 'broadcast_odom_tf': 'True'}.items(),
    )

    move_robot_node = Node(
        package='parcs_stretch_nav2',
        executable='move_robot.py',
        output='screen',
    )

    return LaunchDescription([
        stretch_driver_launch,
        # Give the driver a few seconds to come up before commanding the joints
        TimerAction(period=5.0, actions=[move_robot_node]),
    ])
