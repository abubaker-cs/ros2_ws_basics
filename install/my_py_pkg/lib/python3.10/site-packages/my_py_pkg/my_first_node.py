#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        
        # Create and initialize custom Node
        super().__init__("py_test")
        
        self.counter_ = 0
        
        # Print out message
        self.get_logger().info("Hello ROS2")
        
        self.create_timer(0.5, self.timer_callback)
        
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_ ))

# Main Function
def main(args=None):
    
    # Initialize the communication
    rclpy.init(args=args)
    
    # Create a new object
    node = MyNode()
    
    # 🔥 It is very important, and almost used in all programs
    # Wait / Stay Alive...
    rclpy.spin(node)
    
    # Shutdown the Communication 
    rclpy.shutdown()

# Initilaize the main()
if __name__ == "__main__":
    main()