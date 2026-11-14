#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        self.timer = self.create_timer(5.0, self.print_time)

    def print_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.get_logger().info(f"Текущее время: {current_time}")

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()