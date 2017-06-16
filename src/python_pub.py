#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String 

def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    #pub = rospy.Publisher('01_start_gate_smach_sub', String, queue_size=10)
    pub = rospy.Publisher('start_gate_smach_sub', String, queue_size=10)
    rospy.init_node('data_publisher', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
	#hello_str = "start_gate_complete"
	#hello_str = 1
	derp = '1'
        rospy.loginfo(derp)
        pub.publish(derp)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
