#!/usr/bin/env python

import array as arr
import random
import rospy
from std_msgs.msg import String

def publishMethod():
    arr = ["Mars", "Venus","Moon","Saturn","Pluto","Earth","Jupiter","Uranus","Neptune","Mercury"]
    pub = rospy.Publisher('talker', String, queue_size=10)  # defining the publisher by topic, message type, queue size
    rospy.init_node('publish_node', anonymous = True)       # defining the ros node - publish node
    rate = rospy.Rate(10)                                   # 10hz frequency at which publishing
    while not rospy.is_shutdown():                          
        publishString = "This is being publshed"            # variable
        rospy.loginfo("Data is being to sent to " + arr[(random.randint(0,9))])                 # to print on the terminal
        pub.publish(publishString)                          # publishing
        rate.sleep()

if __name__ == '__main__':
    try:
        publishMethod()
    except rospy.ROSInterruptException:
        pass  
