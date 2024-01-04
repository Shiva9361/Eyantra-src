#!/usr/bin/env python3
from threading import Thread
import time
import rclpy
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.node import Node
#from moveit_msgs.msg import CollisionObject
from pymoveit2 import MoveIt2
from pymoveit2.robots import ur5
from tf2_ros import TransformListener, Buffer

from controller_manager_msgs.srv import SwitchController
from ur_msgs.srv import SetIO

from linkattacher_msgs.srv import AttachLink, DetachLink
from geometry_msgs.msg import TwistStamped

class TFListenerNode(Node):
    
    def __init__(self):
        super().__init__("tf_listener_node")
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.callback_group = ReentrantCallbackGroup()
        self.gripper_control = self.create_client(AttachLink, '/GripperMagnetON')
        self.gripper_control2 = self.create_client(DetachLink, '/GripperMagnetOFF')
        self.__contolMSwitch = self.create_client(SwitchController, "/controller_manager/switch_controller")
        self.moveit2 = MoveIt2(
            node=self,
            joint_names=ur5.joint_names(),
            base_link_name=ur5.base_link_name(),
            end_effector_name=ur5.end_effector_name(),
            group_name=ur5.MOVE_GROUP_ARM
        )
        self.servo_pub = self.create_publisher(TwistStamped, "/servo_node/delta_twist_cmds", 10)
        self.target_frames = ['obj_3','obj_1','obj_49'] # read from param
        self.visited_frames = set()  # Keep track of visited TF frames
        self.declare_parameter(
        "joint_positions1",
        [
            -0.027,
            -1.803,
            -1.3658,
            -3.039,
            -1.52,
            3.15
        ],
    )
    
        
        self.declare_parameter(
        "initial_positions",
        [
            0.0,
            -2.398,
            2.43,
            -3.15,
            -1.58,
            3.15
        ],
    )
      
    
    def gripper_call(self, state):
        '''
        based on the state given as i/p the service is called to activate/deactivate
        pin 16 of TCP in UR5
        i/p: node, state of pin:Bool
        o/p or return: response from service call
        '''
        gripper_control = self.create_client(SetIO, '/io_and_status_controller/set_io')
        while not gripper_control.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('EEF Tool service not available, waiting again...')
        req         = SetIO.Request()
        req.fun     = 1
        req.pin     = 16
        req.state   = float(state)
        gripper_control.call_async(req)
        return state
    def attach(self,objec):
        while not self.gripper_control.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('EEF service not available, waiting again...')

        req = AttachLink.Request()
        req.model1_name =  objec     
        req.link1_name  = 'link'       
        req.model2_name =  'ur5'       
        req.link2_name  = 'wrist_3_link'  

        self.gripper_control.call_async(req)

        
    def detach(self,objec):
        while not self.gripper_control2.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('EEF service not available, waiting again...')

        req = DetachLink.Request()
        req.model1_name =  objec     
        req.link1_name  = 'link'       
        req.model2_name =  'ur5'       
        req.link2_name  = 'wrist_3_link'  

        self.gripper_control2.call_async(req)
    def mode_change(self):
        switchParam = SwitchController.Request()
        switchParam.activate_controllers = ["scaled_joint_trajectory_controller"] # for normal use of moveit
        switchParam.deactivate_controllers = ["forward_position_controller"] # for servoing
        switchParam.strictness = 2
        switchParam.start_asap = False

        # calling control manager service after checking its availability
        while not self.__contolMSwitch.wait_for_service(timeout_sec=5.0):
            self.get_logger().warn(f"Service control Manager is not yet available...")
        self.__contolMSwitch.call_async(switchParam)
        self.get_logger().info("[CM]: Switching Complete")


    def move_to_tf_pose(self, target_frame):
        if target_frame not in self.visited_frames:
            try:
                pre_transform = transform = self.tf_buffer.lookup_transform(
                    'base_link', "pre_obj_"+target_frame.split("_")[-1], rclpy.time.Time(), rclpy.duration.Duration(seconds=1)
                )
                transform = self.tf_buffer.lookup_transform(
                    'base_link', target_frame, rclpy.time.Time(), rclpy.duration.Duration(seconds=1)
                )
                """
                Adding correction
                """

                """x_cor = 0.0
                y_cor = 0.0
                z_cor = 0.0
                if transform.transform.rotation.x <0.6 and transform.transform.rotation.x > .4 and transform.transform.rotation.y <0.6  and transform.transform.rotation.y >0.4:
                    x_cor = 0.1
                elif transform.transform.rotation.x >0.65 and transform.transform.rotation.x < 0.75:
                    y_cor = -0.1
                else:
                    y_cor = 0.1"""
                """ee_t = self.tf_buffer.lookup_transform(
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)
                )"""
                
                #z_servo_dis = abs(ee_t.transform.translation.z-transform.transform.translation.z)
                position = [pre_transform.transform.translation.x, pre_transform.transform.translation.y, pre_transform.transform.translation.z]
                orientation = [pre_transform.transform.rotation.x, pre_transform.transform.rotation.y,
                               pre_transform.transform.rotation.z, pre_transform.transform.rotation.w]
                self.get_logger().info(f"Moving to position: {position}, orientation: {orientation}")
                
                self.moveit2.move_to_pose(position=position, quat_xyzw=orientation)
                self.moveit2.wait_until_executed() 

                position = [transform.transform.translation.x, transform.transform.translation.y, transform.transform.translation.z]
                orientation = [transform.transform.rotation.x, transform.transform.rotation.y,
                               transform.transform.rotation.z, transform.transform.rotation.w]
                self.get_logger().info(f"Moving to position: {position}, orientation: {orientation}")
                
                self.moveit2.move_to_pose(position=position, quat_xyzw=orientation)
                self.moveit2.wait_until_executed() 

                objc = "box"+target_frame.split("_")[-1]
                self.attach(objc)

                position = [pre_transform.transform.translation.x, pre_transform.transform.translation.y, pre_transform.transform.translation.z]
                orientation = [pre_transform.transform.rotation.x, pre_transform.transform.rotation.y,
                               pre_transform.transform.rotation.z, pre_transform.transform.rotation.w]
                self.get_logger().info(f"Moving to position: {position}, orientation: {orientation}")
                
                self.moveit2.move_to_pose(position=position, quat_xyzw=orientation)
                self.moveit2.wait_until_executed() 
                
                
                """msg = TwistStamped()
                msg.header.stamp = self.get_clock().now().to_msg()
                msg.header.frame_id = ur5.base_link_name()
                msg.twist.linear.x = 0.0
                msg.twist.linear.y = 0.0
                msg.twist.linear.z = 0.2
                msg.twist.angular.x = 0.0
                msg.twist.angular.y = 0.0
                msg.twist.angular.z = 0.0
                #self.servo_pub.publish(msg)"""
                """val = self.tf_buffer.lookup_transform(
                    
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)).transform.translation.z - transform.transform.translation.z
                
                while(abs(val)>0.02):
                    if val<0:
                        msg.twist.linear.z = 0.2
                    else:
                        msg.twist.linear.z = -0.2
                    msg.header.stamp = self.get_clock().now().to_msg()
                    self.servo_pub.publish(msg)
                    val = self.tf_buffer.lookup_transform(
                    
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)).transform.translation.z - transform.transform.translation.z
                    
                self.get_logger().info("Servoing z done")"""
                
                """msg.twist.linear.z = 0.0

                val_y = (self.tf_buffer.lookup_transform(
                    
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)).transform.translation.y - transform.transform.translation.y)
                
                val_x = (self.tf_buffer.lookup_transform(
                    
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)).transform.translation.x - transform.transform.translation.x)
                
                while(abs(val_x)>0.02 or abs(val_y)>0.02):
                    if val_x<0:
                        msg.twist.linear.x = 0.2
                    else:
                        msg.twist.linear.x = -0.2
                    if val_y<0:
                        msg.twist.linear.y = 0.2
                    else:
                        msg.twist.linear.y = -0.2
                    if abs(val_x)<=0.02:
                        msg.twist.linear.x = 0.0
                    if abs(val_y)<=0.02:
                        msg.twist.linear.y = 0.0
                    msg.header.stamp = self.get_clock().now().to_msg()
                    self.servo_pub.publish(msg)
                    
                    val_y = (self.tf_buffer.lookup_transform(
                    
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)).transform.translation.y - transform.transform.translation.y)
                
                    val_x = (self.tf_buffer.lookup_transform(
                    
                    'base_link', 'ee_link', rclpy.time.Time(), rclpy.duration.Duration(seconds=1)).transform.translation.x - transform.transform.translation.x)
                
                msg.twist.linear.x = 0.0
                msg.twist.linear.y = 0.0
                msg.twist.linear.z = 0.0
                self.servo_pub.publish(msg)
                self.get_logger().info("Servoing x,y done")"""
                
                # Mark the frame as visited
                self.visited_frames.add(target_frame) 
                
                #time.sleep(2)
                
                
                """
                position = [transform.transform.translation.x, transform.transform.translation.y, transform.transform.translation.z]
                orientation = [transform.transform.rotation.x, transform.transform.rotation.y,
                               transform.transform.rotation.z, transform.transform.rotation.w]
                self.get_logger().info(f"Moving to position: {position}, orientation: {orientation}")
                self.moveit2.move_to_pose(position=position, quat_xyzw=orientation)
                self.visited_frames.add(target_frame)  # Mark the frame as visited
                self.moveit2.wait_until_executed()
                """
                
                """
                position = [ee_t.transform.translation.x, ee_t.transform.translation.y, transform.transform.translation.z]
                orientation = [transform.transform.rotation.x, transform.transform.rotation.y,
                               transform.transform.rotation.z, transform.transform.rotation.w]
                self.get_logger().info(f"Moving to position: {position}, orientation: {orientation}")
                self.moveit2.move_to_pose(position=position, quat_xyzw=orientation)
                self.visited_frames.add(target_frame)  # Mark the frame as visited
                self.moveit2.wait_until_executed()  """
                
                
                """state = 0
                self.gripper_call(state)"""
                # Move to the corresponding joint positions
                
                
                
                
                joint_positions = (self.get_parameter(f"joint_positions1").get_parameter_value().double_array_value)
                self.get_logger().info(f"Moving to {{joint_positions: {list(joint_positions)}}}")
                self.moveit2.move_to_configuration(joint_positions)
                self.moveit2.wait_until_executed()
                
                self.detach(objc)
                #state = 1
                #self.gripper_call(state)
                
                joint_positions = (self.get_parameter(f"initial_positions").get_parameter_value().double_array_value)
                self.get_logger().info(f"Moving to {{joint_positions: {list(joint_positions)}}}")
                self.moveit2.move_to_configuration(joint_positions)
                self.moveit2.wait_until_executed()
                #time.sleep(5)

            except Exception as e:
                self.get_logger().warn(f"Failed to get TF data for {target_frame}: {e}")

def main():
    rclpy.init()

    node = TFListenerNode()
    
    

    executor = rclpy.executors.MultiThreadedExecutor(2)
    executor.add_node(node)
    executor_thread = Thread(target=executor.spin, daemon=True, args=())
    executor_thread.start()

    try:
        while rclpy.ok():
            for target_frame in node.target_frames:
                node.move_to_tf_pose(target_frame)
                
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()