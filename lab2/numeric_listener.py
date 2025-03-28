import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class NumericListener(Node):
    def __init__(self):
        super().__init__('numeric_listener')

        # subscriber for the /chatter topic
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        # subscriber for the /numeric_chatter topic
        self.numeric_subscription = self.create_subscription(Int8, 'numeric_chatter', self.numeric_callback, 10)
        self.numeric_subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')

    def numeric_callback(self, msg):
        self.get_logger().info(f'I heard numeric value: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    # listener = Listener()
    numeric_listener = NumericListener()
    rclpy.spin(numeric_listener)


if __name__ == '__main__':
    main()
