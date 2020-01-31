#!/usr/bin/env python
#import librairies
import rospy
from geometry_msgs.msg import Twist

#define the function
def vitesse():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True) # create node
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  # publish the node created on /turtle1/cmd_vel topic
    vel_msg = Twist() # define the structure of the message 
    
    v_max=rospy.get_param("max") # get max value from vitesse.yaml
    v_min=rospy.get_param("min") # get min value from vitesse.yaml
  
    v_donne = input("write your speed:") # user set the speed value in the console
  
    while v_donne >= v_max or v_donne <= v_min : # repeat the test : v_donne it should be less then or equal to v_max or greater then or equal to v_min
     if v_donne >= v_max :
      v_donne = input("Too fast write again your speed :") # user can give an other v_donne if it's greater then or equal v_max
    
     if v_donne <= v_min:
      v_donne = input("Too slow write again your speed :") # user can give an other v_donne if it's less then or equal v_min
     
   
    print ("your speed is perfect") 
    print v_donne # show the value of the turtlesim speed
      
    #use linear components
    vel_msg.linear.x=v_donne # set the value
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
   
    while not rospy.is_shutdown():# while the node is not interrupted
      velocity_publisher.publish(vel_msg) # publish the message
   
  

if __name__ == '__main__':
    try:
        # Testing the function
        vitesse()
    except rospy.ROSInterruptException: # interruption with Ctrl+C
        pass
