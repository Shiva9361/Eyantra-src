#!/usr/bin/env python3

# Team ID:          [CL#2098]
# Author List:      [D Vishnu Aravind , Bhuvan D, Shivadharshan S]		

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
from ebot_docking.srv import DockSw
from linkattacher_msgs.srv import AttachLink
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

class Docker1(Node):
	def __init__(self):
		super().__init__("Docker_Rack_1")
		self.navigator = BasicNavigator()
		self.dock = self.create_client(DockSw,'dock')
		self.req = DockSw.Request()
	def initial(self):
		self.initial_pose = PoseStamped()
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

	def move_to_goal(self,pos_x,pos_y,or_x,or_y,or_z,or_w,dock):
		self.goal_pose1 = PoseStamped()
		self.goal_pose1.header.frame_id = 'map'
		self.goal_pose1.header.stamp = self.navigator.get_clock().now().to_msg()
		self.goal_pose1.pose.position.x = pos_x
		self.goal_pose1.pose.position.y = pos_y
		self.goal_pose1.pose.orientation.x =  or_x
		self.goal_pose1.pose.orientation.y =  or_y
		self.goal_pose1.pose.orientation.z =  or_z
		self.goal_pose1.pose.orientation.w =  or_w

		self.navigator.goToPose(self.goal_pose1)
		while (not self.navigator.isTaskComplete()) :
			print("Processing",end="\r")
	
		result = self.navigator.getResult()
		if result == TaskResult.SUCCEEDED:
			print('Goal succeeded!')
			if dock:
				self.req.linear_dock = True
				self.future = self.dock.call_async(self.req)
				rclpy.spin_until_future_complete(self, self.future)
				self.get_logger().info("done")

		elif result == TaskResult.CANCELED:
			print('Goal was canceled!')
		elif result == TaskResult.FAILED:
			print('Goal failed!')


def main():
	rclpy.init()
	
	docker = Docker1()
	executor = MultiThreadedExecutor()
	executor.add_node(docker)
	


	docker.initial()
	print("Initial Done")
	docker.move_to_goal(0.535130,4.516938,0.0,-0.998617,0.0,0.052582,True)
	print("Goal 1")
	docker.move_to_goal(0.85,-2.455,0.0,1.0,0.0,0.0,False)

	docker.move_to_goal(1.15,-2.445,0.0,1.0,0.0,0.0,False)
	"""goal_pose1.pose.position.x = 0.535130
	goal_pose1.pose.position.y = 4.516938

	goal_pose1.pose.orientation.x =  0.0
	goal_pose1.pose.orientation.y =  -0.998617
	goal_pose1.pose.orientation.z =  0.0
	goal_pose1.pose.orientation.w =  0.052582"""
		
        

        
	"""
		goal_pose2 = PoseStamped()
		goal_pose2.header.frame_id = 'map'
		goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
		goal_pose2.pose.position.x =  0.85
		goal_pose2.pose.position.y = -2.455

		goal_pose2.pose.orientation.x =  0.0
		goal_pose2.pose.orientation.y =  1.0
		goal_pose2.pose.orientation.z =  0.0
		goal_pose2.pose.orientation.w =  0.0
	"""
	"""	goal_pose3 = PoseStamped()
	goal_pose3.header.frame_id = 'map'
	goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
	goal_pose3.pose.position.x =  1.15
	goal_pose3.pose.position.y = -2.455

	goal_pose3.pose.orientation.x =  0.0
	goal_pose3.pose.orientation.y =  1.0
	goal_pose3.pose.orientation.z =  0.0
	goal_pose3.pose.orientation.w =  0.0"""
	
	
	
	
	executor.spin()
	docker.destroy_node()
	rclpy.shutdown()

if __name__ == "__main__":
	main()	




