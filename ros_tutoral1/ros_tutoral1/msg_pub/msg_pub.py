import rclpy
from rclpy import qos
from rclpy import subscription
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from turtle_msg_interface.msg import RadVelDir
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult


class RadVelDirPublisher(Node):

    def __init__(self):
        super().__init__('radveldir_publisher')
        qos_profile = qos_profile = QoSProfile(depth=10)
        self.declare_parameter('radius', 1.0)
        self.radius = self.get_parameter('radius').value
        self.declare_parameter('velocity', 1.0)
        self.velocity= self.get_parameter('velocity').value
        self.declare_parameter('direction', True)
        self.direction = self.get_parameter('direction').value
        self.add_on_set_parameters_callback(self.update_parameter)

        self.rad_vel_dir_publisher = self.create_publisher(
            RadVelDir,
            'radius_velocity_direction',
            qos_profile
        )

        self.timer = self.create_timer(1.0, self.publish_rad_vel_dir)
        
    def publish_rad_vel_dir(self):
        msg = RadVelDir()
        msg.radius = float(self.radius)
        msg.velocity = float(self.velocity)
        msg.direction = self.direction

        self.str_dir = 'CounterClockwise'
        if not self.direction:
            self.str_dir = 'Clockwise'

        self.rad_vel_dir_publisher.publish(msg)
        self.get_logger().info('Published Rad: {0}, Vel: {1}, Dir: {2}'.format(self.radius, self.velocity, self.str_dir))

    def update_parameter(self, params):
        for param in params:
            if param.name == 'radius' and param.type_ == Parameter.Type.DOUBLE:
                self.radius = param.value
            elif param.name == 'velocity' and param.type_ == Parameter.Type.DOUBLE:
                self.velocity = param.value
            elif param.name == 'direction' and param.type_ == Parameter.Type.BOOL:
                self.direction == param.value
        
        return SetParametersResult(successful = True)

def main(args=None):
    rclpy.init(args=args)
    try:
        node = RadVelDirPublisher()
        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            node.get_logger().info('Keyboard Interrupt (SIGINT)')
        finally:
            node.destroy_node()
    finally:
        rclpy.shutdown

if __name__=='__main__':
    main()