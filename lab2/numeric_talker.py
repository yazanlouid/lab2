import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8

class NumericTalker(Node):
    def __init__(self):
        super().__init__('numeric_talker')

        # publisher for /chatter topic (string message)
        self.publisher = self.create_publisher(String, 'chatter', 10)
        # publisher for /numeric_chatter topic (Int8 message)
        self.numeric_publisher = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0

    def talker_callback(self):
        # publish to the /chatter topic
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

        # pubish to the /numeric_chatter topic
        numeric_msg = Int8()
        numeric_msg.data = self.counter
        self.numeric_publisher.publish(numeric_msg)
        self.get_logger().info(f'Publishing numeric value: {numeric_msg.data}')

        # increment and reset counter
        self.counter += 1
        if self.counter > 127:
            self.counter = 0

def main(args=None):
    rclpy.init(args=args)
    # talker = Talker()
    numeric_talker = NumericTalker()
    rclpy.spin(numeric_talker)


if __name__ == '__main__':
    main()


