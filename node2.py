import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Ros2 nodes publish messages to a topic which then the other node can see
# or publish to that topic as well
# If you need something to compare this to do research on MQTT communication

# This node subscribes to the data published from Node A and recieves it
class NodeB_Subscriber(Node):
    def __init__(self):
        super().__init__('node_b_subscriber')
        self.subscription = self.create_subscription(
            String, 'chatter', self.listener_callback, 10)
        self.get_logger().info("Node B Subscriber has started.")

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main():
    rclpy.init()
    node = NodeB_Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
