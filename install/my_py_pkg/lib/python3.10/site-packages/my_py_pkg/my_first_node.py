#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Main Function
def main(args=None):
    
    # Initialize the communication
    rclpy.init(args=args)
    
    # Create custom Node
    node = Node("py_test")
    
    # Print out message
    node.get_logger().info("Hello ROS2")
    
    # 🔥 It is very important, and almost used in all programs
    # Wait / Stay Alive...
    rclpy.spin(node)
    
    # Shutdown the Communication 
    rclpy.shutdown()

# Initilaize the main()
if __name__ == "__main__":
    main()