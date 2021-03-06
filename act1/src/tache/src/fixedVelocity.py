#!/usr/bin/env python
#import librairies
import rospy
from geometry_msgs.msg import Twist

#define the function
def vitesse():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True) # create node
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # publish the node created on /turtle1/cmd_vel topic
    vel_msg = Twist() # define the structure of the message 

  
    #use linear components
    vel_msg.linear.x=rospy.get_param("fixed") # get the parameter from vitesse.yaml
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
   
    print vel_msg.linear.x #print the value getted 
   
    while not rospy.is_shutdown(): #while the node is not interrupted
        velocity_publisher.publish(vel_msg) # publish the message
        

if __name__ == '__main__':
    try:
        # Testing the function
        vitesse()
    except rospy.ROSInterruptException:  # interruption with Ctrl+C
        pass
