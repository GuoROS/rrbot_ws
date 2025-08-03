import rclpy
from rclpy.node import  Node
from  control_msgs.msg import JointJog

class RRBotPositionPublisher(Node):
    def __init__(self,name):
        super().__init__(name)
        self.postion_publisher = self.create_publisher(JointJog, "my_controller/reference", 10)
        self.msg = JointJog()
        self.msg.joint_names = ['joint1', 'joint2']
        self.datas =[[0.0, 0.0],[-1.0, -1.0],[0.0, 0.0],[1.0, 1.0]]
        self.i = 0

        self.timer = self.create_timer(3, self.timer_callback)

    def timer_callback(self):
        self.msg.displacements = self.datas[self.i % 4]
        self.i += 1
        self.postion_publisher.publish(self.msg)


def main(args=None):
    rclpy.init(args=args)
    node =  RRBotPositionPublisher("rrbot_pos_pub")
    rclpy.spin(node)
    rclpy.shutdown()