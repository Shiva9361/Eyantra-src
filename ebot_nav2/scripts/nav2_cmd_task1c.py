#!/usr/bin/env python3

# Team ID:          [CL#2098]
# Author List:      [D Vishnu Aravind , Bhuvan D]		

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import time
from ebot_docking.srv import DockSw
from linkattacher_msgs.srv import AttachLink
from rclpy.node import Node

def main():
	rclpy.init()

	navigator = BasicNavigator()

    
	initial_pose = PoseStamped()
	initial_pose.header.frame_id = 'map'
	initial_pose.header.stamp = navigator.get_clock().now().to_msg()
	initial_pose.pose.position.x = 0.0
	initial_pose.pose.position.y = 0.0
	initial_pose.pose.orientation.x = 0.0
	initial_pose.pose.orientation.y = 0.0
	initial_pose.pose.orientation.z = 0.0
	initial_pose.pose.orientation.w = 0.0

	navigator.setInitialPose(initial_pose)
	navigator.waitUntilNav2Active()

	goal_pose1 = PoseStamped()
	goal_pose1.header.frame_id = 'map'
	goal_pose1.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose1.pose.position.x = 0.535130
	goal_pose1.pose.position.y = 4.516938

	goal_pose1.pose.orientation.x =  0.0
	goal_pose1.pose.orientation.y =  -0.998617
	goal_pose1.pose.orientation.z =  0.0
	goal_pose1.pose.orientation.w =  0.052582

	navigator.goToPose(goal_pose1)
	while (not navigator.isTaskComplete()) :
	   
	   print("Processing",end="\r")
	
	result = navigator.getResult()
	if result == TaskResult.SUCCEEDED:
		print('Goal 1 succeeded!')
	elif result == TaskResult.CANCELED:
		print('Goal was canceled!')
	elif result == TaskResult.FAILED:
		print('Goal failed!')
		
	time.sleep(22)
	
	goal_pose2_1 = PoseStamped()
	goal_pose2_1.header.frame_id = 'map'
	goal_pose2_1.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose2_1.pose.position.x =  0.188365
	goal_pose2_1.pose.position.y = -2.080885

	goal_pose2_1.pose.orientation.x =  0.0
	goal_pose2_1.pose.orientation.y =  -0.989121
	goal_pose2_1.pose.orientation.z =  0.0
	goal_pose2_1.pose.orientation.w =  0.147102
	navigator.goToPose(goal_pose2_1)
	while (not navigator.isTaskComplete()) :
	   
	   print("Processing",end="\r")
	
	result = navigator.getResult()
	if result == TaskResult.SUCCEEDED:
		print('Goal 2_1 succeeded!')
	elif result == TaskResult.CANCELED:
		print('Goal was canceled!')
	elif result == TaskResult.FAILED:
		print('Goal failed!')	
        


	goal_pose2 = PoseStamped()
	goal_pose2.header.frame_id = 'map'
	goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose2.pose.position.x =  1.05
	goal_pose2.pose.position.y = -2.455

	goal_pose2.pose.orientation.x =  0.0
	goal_pose2.pose.orientation.y =  1.0
	goal_pose2.pose.orientation.z =  0.0
	goal_pose2.pose.orientation.w =  0.000795
	navigator.goToPose(goal_pose2)
	while (not navigator.isTaskComplete()) :
	   
	   print("Processing",end="\r")
	
	result = navigator.getResult()
	if result == TaskResult.SUCCEEDED:
		print('Goal 2 succeeded!')
	elif result == TaskResult.CANCELED:
		print('Goal was canceled!')
	elif result == TaskResult.FAILED:
		print('Goal failed!')	
        
	time.sleep(4)
	
	goal_pose3 = PoseStamped()
	goal_pose3.header.frame_id = 'map'
	goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose3.pose.position.x =  -0.328750
	goal_pose3.pose.position.y =  -2.169140

	goal_pose3.pose.orientation.x =   0.0
	goal_pose3.pose.orientation.y =   0.991037
	goal_pose3.pose.orientation.z =   0.0
	goal_pose3.pose.orientation.w =   0.133586
	navigator.goToPose(goal_pose3)
	while (not navigator.isTaskComplete()) :
	   
	   print("Processing",end="\r")
	
	result = navigator.getResult()
	if result == TaskResult.SUCCEEDED:
		print('Goal 3 succeeded!')
	elif result == TaskResult.CANCELED:
		print('Goal was canceled!')
	elif result == TaskResult.FAILED:
		print('Goal failed!')		
	

	goal_pose4 = PoseStamped()
	goal_pose4.header.frame_id = 'map'
	goal_pose4.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose4.pose.position.x = 1.715638
	goal_pose4.pose.position.y = 2.372627
       
	goal_pose4.pose.orientation.x =    0.0
	goal_pose4.pose.orientation.y =   -0.811021
	goal_pose4.pose.orientation.z =    0.0
	goal_pose4.pose.orientation.w =    0.585017
	navigator.goToPose(goal_pose4)
	while (not navigator.isTaskComplete()) :
	   
	   print("Processing",end="\r")
	
	result = navigator.getResult()
	if result == TaskResult.SUCCEEDED:
		print('Goal 4 succeeded!')
	elif result == TaskResult.CANCELED:
		print('Goal was canceled!')
	elif result == TaskResult.FAILED:
		print('Goal failed!')			

if __name__ == "__main__":
	main()	




