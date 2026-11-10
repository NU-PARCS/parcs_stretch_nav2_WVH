#! /usr/bin/env python3

# Launch the Stretch driver beforehand (or use move_robot.launch.py):
#   ros2 launch stretch_core stretch_driver.launch.py
# See https://docs-arch.hello-robot.com/0.3/ros2/intro_to_hellonode/

import hello_helpers.hello_misc as hm

node = hm.HelloNode.quick_create('move_robot')
log = node.get_logger()

# Lift (meters)
node.move_to_pose({'joint_lift': 0.6}, blocking=True)
log.info('Lift moved to 0.6')
node.move_to_pose({'joint_lift': 0.5}, blocking=True)
log.info('Lift moved to 0.5')

# Arm (meters)
node.move_to_pose({'wrist_extension': 0.1}, blocking=True)
log.info('Arm extended to 0.1')
node.move_to_pose({'wrist_extension': 0.0}, blocking=True)
log.info('Arm retracted to 0.0')

# Wrist yaw (radians)
node.move_to_pose({'joint_wrist_yaw': 0.5}, blocking=True)
log.info('Wrist yaw moved to 0.5')
node.move_to_pose({'joint_wrist_yaw': 0.0}, blocking=True)
log.info('Wrist yaw moved to 0.0')

# Wrist pitch (radians) - dex wrist only
node.move_to_pose({'joint_wrist_pitch': -0.3}, blocking=True)
log.info('Wrist pitch moved to -0.3')
node.move_to_pose({'joint_wrist_pitch': 0.0}, blocking=True)
log.info('Wrist pitch moved to 0.0')

# Wrist roll (radians) - dex wrist only
node.move_to_pose({'joint_wrist_roll': 0.3}, blocking=True)
log.info('Wrist roll moved to 0.3')
node.move_to_pose({'joint_wrist_roll': 0.0}, blocking=True)
log.info('Wrist roll moved to 0.0')

# Gripper
node.move_to_pose({'joint_gripper_finger_left': 0.3}, blocking=True)
log.info('Gripper opened to 0.3')
node.move_to_pose({'joint_gripper_finger_left': 0.0}, blocking=True)
log.info('Gripper moved to 0.0')

# Head pan (radians)
node.move_to_pose({'joint_head_pan': 0.5}, blocking=True)
log.info('Head pan moved to 0.5')
node.move_to_pose({'joint_head_pan': 0.0}, blocking=True)
log.info('Head pan moved to 0.0')

# Head tilt (radians)
node.move_to_pose({'joint_head_tilt': -0.5}, blocking=True)
log.info('Head tilt moved to -0.5')
node.move_to_pose({'joint_head_tilt': 0.0}, blocking=True)
log.info('Head tilt moved to 0.0')

log.info('Done moving all joints')
