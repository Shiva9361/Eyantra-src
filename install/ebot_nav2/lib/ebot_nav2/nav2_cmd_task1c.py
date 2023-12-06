#!/usr/bin/env python3

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import time

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
	goal_pose1.pose.position.x = 0.124078
	goal_pose1.pose.position.y = 4.538481

	goal_pose1.pose.orientation.x =  0.0
	goal_pose1.pose.orientation.y =  0.909297
	goal_pose1.pose.orientation.z =  0.0
	goal_pose1.pose.orientation.w =  -0.416147

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
		
		
	



		

if __name__ == "__main__":
	main()	




