import rclpy
from rclpy.node import Node
from moveit_commander import MoveGroupCommander

class PickPlace(Node):
    def __init__(self):
        super().__init__('pick_place')
        self.arm = MoveGroupCommander('arm')

    def move_to(self, x, y, z):
        pose = self.arm.get_current_pose().pose
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        self.arm.set_pose_target(pose)
        self.arm.go(wait=True)

rclpy.init()
node = PickPlace()
node.move_to(0.3, 0.0, 0.2)  # Example pick position
node.move_to(0.5, 0.0, 0.2)  # Example place position
rclpy.shutdown()
