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
import asyncio
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from tf_transformations import euler_from_quaternion
from ebot_docking.srv import DockSw  # Import custom service message
import math, statistics
#from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from linkattacher_msgs.srv import AttachLink
import time
# Define a class for your ROS2 node
class MyRobotDockingController(Node):

    def __init__(self):
        # Initialize the ROS2 node with a unique name
        super().__init__('my_robot_docking_controller')

        # Create a callback group for managing callbacks
        self.callback_group = ReentrantCallbackGroup()
        #self.event = asyncio.Event()


        # Subscribe to odometry data for robot pose information
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.odometry_callback, 10,callback_group = self.callback_group)

        #self.docker_service = self.create_service(DockSw,'docker',self.docker_callback)

        # Subscribe to ultrasonic sensor data for distance measurements
        self.ultrasonic_rl_sub = self.create_subscription(Range, '/ultrasonic_rl/scan', self.ultrasonic_rl_callback, 10,callback_group = self.callback_group)
        # Add another one here
        self.ultrasonic_rr_sub = self.create_subscription(Range, '/ultrasonic_rr/scan', self.ultrasonic_rr_callback, 10,callback_group= self.callback_group)

        self.docker = self.create_service(DockSw,'dock',self.docker_callback,callback_group=self.callback_group)

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
        self.dock_aligned = False
        
        #self.controller_timer = self.create_timer(0.1, self.controller_loop)
        #         
        
        # 
        # 
        # 
        # 
    """async def waiter(self):
        #rate = self.create_rate(2, self.get_clock())
        
        # Wait until the robot is aligned for docking
        await self.event.wait()"""

    def docker_callback(self,request,response):
        self.get_logger().info("Docking started!")
        self.is_docking = True
        # Create a rate object to control the loop frequency
        self.controller_timer = self.create_timer(0.1, self.controller_loop)
        while self.dock_aligned == False:
            self.get_logger().info("do")
            time.sleep(10)
        # Set the service response indicating success
        response.success = True
        response.message = "Docking control initiated"
        self.dock_aligned = False
        return response

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
        self.get_logger().info("loop")
        # The controller loop manages the robot's linear and angular motion 
        # control to achieve docking alignment and execution
        if self.is_docking:
            dist = self.usrleft_value
            print(dist)
            self.get_logger().info(str(dist))
            yaw_error = abs(3.140003 - self.robot_pose[2])
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
                self.is_docking=False
                cmd_vel.linear.x = 0.0
                cmd_vel.linear.y = 0.0
                cmd_vel.angular.z =0.0
                cmd_vel.angular.y =0.0
                cmd_vel.angular.x =0.0
                self.cmd_vel_pub.publish(cmd_vel)
                print("Bot Docked Successfully")
                self.is_docking = False
                self.dock_aligned = True
                self.event.set()

                

            if(dist > 0.1) and (ori == True):
                cmd_vel.linear.x = -0.23
                cmd_vel.linear.y = -0.23
                self.cmd_vel_pub.publish(cmd_vel)

    """def initial(self):
        self.initial_pose = PoseStamped()
        self.initial_pose.header.frame_id = 'map'
        self.initial_pose.header.frame_id = 'map'
        self.initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        self.initial_pose.pose.position.x = 0.0
        self.initial_pose.pose.position.y = 0.0
        self.initial_pose.pose.orientation.x = 0.0
        self.initial_pose.pose.orientation.y = 0.0
        self.initial_pose.pose.orientation.z = 0.0
        self.initial_pose.pose.orientation.w = 0.0
        self.navigator.setInitialPose(self.initial_pose)
        self.navigator.waitUntilNav2Active()

    def move_to_goal(self,pos_x,pos_y,or_x,or_y,or_z,or_w):
        self.goal_pose1 = PoseStamped()
        self.goal_pose1.header.frame_id = 'map'
        self.goal_pose1.header.stamp = self.navigator.get_clock().now().to_msg()
        self.goal_pose1.pose.position.x = pos_x
        self.goal_pose1.pose.position.y = pos_y
        self.goal_pose1.pose.orientation.x =  or_x
        self.goal_pose1.pose.orientation.y =  or_y
        self.goal_pose1.pose.orientation.z =  or_z
        self.goal_pose1.pose.orientation.w =  or_w
        while (not self.navigator.isTaskComplete()) :
            print("Processing",end="\r")
        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal 1 succeeded!')  
        elif result == TaskResult.CANCELLED:
            print('Goal was canceled!')
        elif result == TaskResult.FAILED:
            print('Goal failed!')  """   

# Main function to initialize the ROS2 node and spin the executor

def main(args=None):
    rclpy.init(args=args)

    my_robot_docking_controller = MyRobotDockingController()

    executor = MultiThreadedExecutor(2)
    executor.add_node(my_robot_docking_controller)

    executor.spin()

    my_robot_docking_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
