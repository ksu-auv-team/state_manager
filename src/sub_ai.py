#!/usr/bin/env python

import roslib;
import rospy
import smach
import smach_ros
from std_msgs.msg import String
recieved = '0'

# define Start Gate
class start_gate(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['start_gate_complete', 'start_gate_null'])
        #self.pub = rospy.Publisher('start_gate_smach_pub', String, queue_size='10')
        #rate = rospy.Rate(.5)
        #self.sub = rospy.Subscriber("start_gate_smach_sub", String, self.callback)
        #rospy.spin()

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        #rospy.loginfo('Executing state start_gate')
        #start_gate_String_pub = 'run_start_gate'
        #self.pub.publish(start_gate_String_pub)
        self.sub = rospy.S
        subscriber("start_gate_smach_sub", String, self.callback)

        if recieved == '0':
            self.sub = rospy.Subscriber("start_gate_smach_sub", String, self.callback)
            rospy.loginfo('execute data: %s', recieved)
            return 'start_gate_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'start_gate_complete'
            else:
                return 'start_gate_null'
        rospy.spin()

#define bouys
class bouys(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['bouy_complete', 'bouy_null'])
        self.pub = rospy.Publisher('bouy_smach_pub', String, queue_size='10')
        rate = rospy.Rate(10)
    
    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id(), data.data)
        recieved = data.data

    def bouy_smach_sub():
        rospy.init_node('bouy_smach_sub', anonymous =True)
        self.sub = rospy.Subscriber("bouy_smach_sub", String, callback)

    def execute(self, userdata):
        rospy.loginfo('Executing state bouy')
        bouy_String_pub = 'run_bouy'
        self.pub.publish(bouy_String_pub)
        rospy.loginfo('running bouys, waiting for confirmation')
        if data.data == 'bouy_complete':
            return 'bouy_complete'
        else:
            return 'bouy_null'

def main():
    rospy.init_node('sub_ai_state_manager')

    #create SMACH state machine
    sm = smach.StateMachine(outcomes=['celebrate'])

    #Open Container
    with sm:
        #add states to the Container
        smach.StateMachine.add('start_gate', start_gate(),
                            transitions={'start_gate_complete':'celebrate', 'start_gate_null':'start_gate'})
        smach.StateMachine.add('bouys', bouys(),
                            transitions={'bouy_complete':'celebrate', 'bouy_null':'bouys'})
    #create Introspection server to view
    sis = smach_ros.IntrospectionServer('smach_server', sm, '/SM_ROOT')
    sis.start()
    
    #Execute SMACH plan
    outcome = sm.execute()

    #Tell ROS to go around again
    rospy.spin()
    #wait for Ctrl+C or end of states to end server
    sis.stop
    
#run the Python code

if __name__ == '__main__':
    main()