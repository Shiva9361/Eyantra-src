#!/usr/bin/env python3

## Overview
# Team ID:          [CL#2098]
# Author List:      [D Vishnu Aravind , Bhuvan D]		

# ###
# This ROS2 script is designed to control a robot's docking behavior with a rack. 
# It utilizes odometry data, ultrasonic sensor readings, and provides docking control through a custom service. 
# The script handles both linear and angular motion to achieve docking alignment and execution.
# ###

# Import necessary ROS2 packages and message types
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from tf_transformations import euler_from_quaternion
from ebot_docking.srv import DockSw  # Import custom service message
import math, statistics
from linkattacher_msgs.srv import AttachLink
import time
# Define a class for your ROS2 node
class MyRobotDockingController(Node):

    def __init__(self):
        # Initialize the ROS2 node with a unique name
        super().__init__('my_robot_docking_controller')

        # Create a callback group for managing callbacks
        self.callback_group = ReentrantCallbackGroup()

        # Subscribe to odometry data for robot pose information
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.odometry_callback, 10)

        # Subscribe to ultrasonic sensor data for distance measurements
        self.ultrasonic_rl_sub = self.create_subscription(Range, '/ultrasonic_rl/scan', self.ultrasonic_rl_callback, 10)
        # Add another one here
        self.ultrasonic_rr_sub = self.create_subscription(Range, '/ultrasonic_rr/scan', self.ultrasonic_rr_callback, 10)

        # Create a ROS2 service for controlling docking behavior, can add another custom service message
        #self.dock_control_srv = self.create_service(DockSw, 'dock_control', self.dock_control_callback)
        
        # Create a publisher for sending velocity commands to the robot
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        #
        self.usrleft_value = 0.0
        self.usrright_value = 0.0
        self.robot_pose = [0.0,0.0,0.0]
        # Initialize all  flags and parameters here
        self.is_docking = False
        
        self.controller_timer = self.create_timer(0.1, self.controller_loop)
        #         
        # 
        # 
        # 
        # 
        # 



    # Callback function for odometry data
    def odometry_callback(self, msg):
        # Extract and update robot pose information from odometry message
        self.robot_pose[0] = msg.pose.pose.position.x
        self.robot_pose[1] = msg.pose.pose.position.y
        quaternion_array = msg.pose.pose.orientation
        orientation_list = [quaternion_array.x, quaternion_array.y, quaternion_array.z, quaternion_array.w]
        _, _, yaw = euler_from_quaternion(orientation_list)
        self.robot_pose[2] = yaw

    # Callback function for the left ultrasonic sensor
    def ultrasonic_rl_callback(self, msg):
        self.usrleft_value = msg.range

    # Callback function for the right ultrasonic sensor
    def ultrasonic_rr_callback(self, msg):
        self.usrright_value = msg.range

    # Utility function to normalize angles within the range of -π to π (OPTIONAL)
    def normalize_angle(self, angle):
        
        pass

    # Main control loop for managing docking behavior

    def controller_loop(self):

        # The controller loop manages the robot's linear and angular motion 
        # control to achieve docking alignment and execution
        if not self.is_docking:
           dist = self.usrleft_value
           print(dist)
           yaw_error = abs(-1.570000 - self.robot_pose[2])
           print(yaw_error)
           ori = False
           cmd_vel = Twist()
           if (yaw_error < 0.05):
             cmd_vel.angular.z = 0.0
             cmd_vel.angular.y = 0.0
             cmd_vel.angular.x = 0.0
             cmd_vel.linear.x = 0.0
             cmd_vel.linear.y = 0.0
             ori = True
             self.cmd_vel_pub.publish(cmd_vel) 
           if (yaw_error > 0.05):
             cmd_vel.angular.z = 0.45 * (yaw_error)
             self.cmd_vel_pub.publish(cmd_vel)
             print("Docking Initiated") 
           if (dist < 0.1) and (ori == True):
             self.is_docking=True
             cmd_vel.linear.x = 0.0
             cmd_vel.linear.y = 0.0
             cmd_vel.angular.z =0.0
             cmd_vel.angular.y =0.0
             cmd_vel.angular.x =0.0
             self.cmd_vel_pub.publish(cmd_vel)
             print("Bot Docked Successfully")
             self.is_docking = True
             my_robot_docking_controller.destroy_node()
             rclpy.shutdown()
           if(dist > 0.1) and (ori == True):
             cmd_vel.linear.x = -0.23
             cmd_vel.linear.y = -0.23
             self.cmd_vel_pub.publish(cmd_vel)
    # Callback function for the DockControl service

# Main function to initialize the ROS2 node and spin the executor
def main(args=None):
    rclpy.init(args=args)

    my_robot_docking_controller = MyRobotDockingController()

    executor = MultiThreadedExecutor()
    executor.add_node(my_robot_docking_controller)

    executor.spin()

    my_robot_docking_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
