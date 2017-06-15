#!/usr/bin/env python

import roslib;
import rospy
import smach
import smach_ros
from std_msgs.msg import String

# define Start Gate
class start_gate(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['start_gate_complete', 'start_gate_null'])
        self.pub = rospy.Publisher('start_gate_smach_pub', String, queue_size='10')
        rate = rospy.Rate(10)

    def callback(data):
        rospy.loginfo(rospy.get_caller_id(), data.data)
        recieved = data.data 

    def start_gate_smach_sub():
        rospy.init_node('start_gate_smach_sub', anonymous =True)
        self.sub = rospy.Subscriber("start_gate_smach_sub", String, callback)

    def execute(self, userdata):
        rospy.loginfo('Executing state start_gate')
        start_gate_string_pub = 'run_start_gate'
        self.pub.publish(start_gate_string_pub)
        if recieved = 'start_gate_complete'
            rospy.infolog(data.data)
            return 'start_gate_complete'
        else:
            return 'start_gate_null'

#define bouys
class bouys(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['bouy_complete', 'bouy_null'])
        self.pub = rospy.Publisher('bouy_smach_publisher', String, queue_size='10')
        self.sub = rospy.Subscriber("bouy_smach_pub", String, callback)
        rate = rospy.Rate(10)
    
    def callback(data)
        rospy.loginfo(rospy.get_caller_id(), data.data)

    def execute(self, userdata):
        rospy.loginfo('Executing state bouy')   
        bouy_string_pub = 'run_bouy'
        self.pub.publish(bouy_string_pub)
        if data.data = 'bouy_complete'
            return 'bouy_complete'
        else:
            return 'bouy_null'

def main()
    rospy.init_node('sub_ai_state_manager')

    #create SMACH state machine
    sm = smach.StateMachine(outcomes=['celebrate'])

    #Open Container
    with sm:
        #add states to the Container
        smach.StateMachine.add('start_gate', start_gate())
                                transitions={'start_gate_complete':'bouy_null'}
        smach.StateMachine.add('bouys', bouys())
                                transitions={'bouy_complete':'celebrate'}
    #create Introspection server to view
    sis = smach_ros.IntrospectionServer('smach_server', sm, '/SM_ROOT')
    sis.start_gate
    
    #Execute SMACH plan
    sm.execute

    #Tell ROS to go around again
    rospy.spin()
    #wait for Ctrl+C or end of states to end server
    sis.stop
    
#run the Python code

if __name__ == '__main__':
    main()