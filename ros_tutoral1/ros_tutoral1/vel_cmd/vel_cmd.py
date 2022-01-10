import rclpy
from rclpy.node import Node
from rclpy.node import QoSProfile
from std_msgs.msg import String
from turtle_msg_interface.msg import RadVelDir
from geometry_msgs.msg import Twist, Vector3

class TurtleGoRound(Node):

    def __init__(self):
        self.radius = 0.0
        self.velocity = 0.0
        self.direction = True
        
        super().__init__('turtle_go_round')
        qos_profile = QoSProfile(depth =10)
        self.turtle_msg = self.create_subscription(
            RadVelDir,
            'radius_velocity_direction',
            self.turtle_sub_msg,
            qos_profile
        )

        self.turtle_pub = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            qos_profile
        )
        self.timer = self.create_timer(1.0, self.publish_turtle_msg)

    def turtle_sub_msg(self, msg):
        self.radius = msg.radius
        self.velocity = msg.velocity
        self.direction = msg.direction
        self.str_dir = 'CounterClockwise'
        if not self.direction:
            self.str_dir = 'Clockwise'

        self.get_logger().info('Subscribed R: {0}, V: {1}, D: {2}'.format(self.radius, self.velocity, self.str_dir))

    def publish_turtle_msg(self):
        self.linear_vel = Vector3()
        self.angular_vel = Vector3()
        self.twist = Twist()

        self.linear_vel.x = self.velocity
        self.linear_vel.y = 0.0
        self.linear_vel.z = 0.0
        self.angular_vel.x = 0.0
        self.angular_vel.y = 0.0
        if self.radius > 0.0:
            self.angular_vel.z = self.velocity/self.radius
            if not self.direction:
                self.angular_vel.z *= -1
        else:
            self.linear_vel.x = 0.0
            self.angular_vel.z = 0.0
        self.twist.linear = self.linear_vel
        self.twist.angular = self.angular_vel

        self.turtle_pub.publish(self.twist)

        self.get_logger().info('Published Twist: {0}'.format(self.twist))

def main(args=None):
    rclpy.init(args=args)
    node = TurtleGoRound()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
