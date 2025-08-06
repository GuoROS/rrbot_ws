import rclpy
from rclpy.node import  Node
from  control_msgs.msg import JointJog

class RRBotPositionPublisher(Node):
    def __init__(self,name):
        super().__init__(name)
        self.position_subscriber = self.create_subscription(JointJog, "my_controller/state", self.state_callback, 10)
        # self.msg = JointJog()
        # self.msg.joint_names = ['joint1', 'joint2']
        # self.datas =[[0.0, 0.0],[-1.0, -1.0],[0.0, 0.0],[1.0, 1.0]]
        # self.i = 0

        # self.timer = self.create_timer(3, self.timer_callback)

    def state_callback(self, msg):
        self.get_logger().info(f"time: {msg.header.stamp.sec}--------")
        for i in range(0,2):
            self.get_logger().info(f"{msg.joint_names[i]}:{msg.displacements[i]}")
        self.get_logger().info('-----------------------')



def main(args=None):
    rclpy.init(args=args)
    node =  RRBotPositionPublisher("rrbot_pos_sub")
    rclpy.spin(node)
    rclpy.shutdown()