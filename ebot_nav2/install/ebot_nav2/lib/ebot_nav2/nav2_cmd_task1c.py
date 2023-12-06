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
	goal_pose1.pose.position.x = 1.8
	goal_pose1.pose.position.y = 1.5

	goal_pose1.pose.orientation.x = 0.0
	goal_pose1.pose.orientation.y = 0.7068252
	goal_pose1.pose.orientation.z = 0.0
	goal_pose1.pose.orientation.w = 0.7073882

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
		
	print(goal_pose1.pose.position.x,goal_pose1.pose.position.y,goal_pose1.pose.orientation.x,goal_pose1.pose.orientation.y,goal_pose1.pose.orientation.z,goal_pose1.pose.orientation.w)
	

	
	goal_pose2 = PoseStamped()
	goal_pose2.header.frame_id = 'map'
	goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose2.pose.position.x = 2.0
	goal_pose2.pose.position.y = -7.0
	goal_pose2.pose.orientation.x = 0.0
	goal_pose2.pose.orientation.y = -0.7068252
	goal_pose2.pose.orientation.z = 0.0
	goal_pose2.pose.orientation.w = 0.7073882
	
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
		
	print(goal_pose2.pose.position.x,goal_pose2.pose.position.y,goal_pose2.pose.orientation.x,goal_pose2.pose.orientation.y,goal_pose2.pose.orientation.z,goal_pose2.pose.orientation.w)
	
	goal_pose3 = PoseStamped()
	goal_pose3.header.frame_id = 'map'
	goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose3.pose.position.x = -3.0
	goal_pose3.pose.position.y = 2.5
	goal_pose3.pose.orientation.x = 0.0
	goal_pose3.pose.orientation.y = 0.7068252
	goal_pose3.pose.orientation.z = 0.0
	goal_pose3.pose.orientation.w = 0.7073882


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
		

		

if __name__ == "__main__":
	main()	




