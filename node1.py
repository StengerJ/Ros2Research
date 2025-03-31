import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Ros2 nodes publish messages to a topic which then the other node can see
# or publish to that topic as well
# If you need something to compare this to do research on MQTT communication

# This node publishes to a topic with the message, Hello from Node A!
class NodeA_Publisher(Node):
    def __init__(self):
        super().__init__('node_a_publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.get_logger().info("Node A Publisher has started.")

    def publish_message(self):
        msg = String()
        msg.data = "Hello from Node A!"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main():
    rclpy.init()
    node = NodeA_Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
