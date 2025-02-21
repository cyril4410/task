from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import FindPackageShare

def generate_launch_description():
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('gazebo_ros'), '/launch/gazebo.launch.py'
        ])
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open('/home/cyril/ros2_ws/src/my_robot_description/urdf/robot.urdf.xacro').read()}]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
    ])
