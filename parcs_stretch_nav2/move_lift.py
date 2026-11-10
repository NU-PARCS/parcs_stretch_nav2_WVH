#! /usr/bin/env python3

"""
Simple HelloNode example: moves Stretch's lift to 0.4 m.

Launch the Stretch driver beforehand:
    ros2 launch stretch_core stretch_driver.launch.py

Then run:
    ros2 run parcs_stretch_nav2 move_lift.py

See https://docs-arch.hello-robot.com/0.3/ros2/intro_to_hellonode/
"""

import hello_helpers.hello_misc as hm


def main():
    node = hm.HelloNode.quick_create('move_lift')
    node.move_to_pose({'joint_lift': 0.4}, blocking=True)
    node.get_logger().info('Lift moved to 0.4 m')


if __name__ == '__main__':
    main()
