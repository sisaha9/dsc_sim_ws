import rclpy
from rclpy.node import Node

from lgsvl_msgs.msg import CanBusData
from nav_msgs.msg import Odometry
import pymap3d



class LgsvlInterface(Node):

    def __init__(self):
        super().__init__('lgsvl_interface_node')
        self.declare_parameter("origin.lat", 0.0)
        self.declare_parameter("origin.lon", 0.0)
        self.declare_parameter("origin.alt", 0.0)
        self.localization_sub = self.create_subscription(
            CanBusData,
            'canbus',
            self.localization_callback,
            10)
        self.localization_sub  # prevent unused variable warning
        self.odom_publisher = self.create_publisher(Odometry, 'odometry', 10)

    def localization_callback(self, msg):
        e, n, u = pymap3d.geodetic2enu(
            msg.gps_latitude, msg.gps_longitude, msg.gps_altitude, self.get_parameter("origin.lat").get_parameter_value().double_value, self.get_parameter("origin.lon").get_parameter_value().double_value, self.get_parameter("origin.alt").get_parameter_value().double_value)
        odom_msg = Odometry()
        odom_msg.header.frame_id = 'map'
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.pose.pose.position.x = e
        odom_msg.pose.pose.position.y = n
        odom_msg.pose.pose.position.z = u
        odom_msg.pose.pose.orientation = msg.orientation
        odom_msg.twist.twist.linear = msg.linear_velocities
        self.odom_publisher.publish(odom_msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = LgsvlInterface()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()