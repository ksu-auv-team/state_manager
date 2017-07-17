#!/usr/bin/env python

import roslib;
import rospy
import smach
import smach_ros
import threading
from std_msgs.msg import String
recieved = '0'

# define Start Gate
class start_gate(smach.State):

    def __init__(self):
        global recieved
        recieved = '0'
        smach.State.__init__(self, outcomes=['start_gate_complete', 'start_gate_null'])
        self.pub = rospy.Publisher('start_gate_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state start_gate')
        start_gate_String_pub = 'run_start_gate'
        self.pub.publish(start_gate_String_pub)
        self.sub = rospy.Subscriber("start_gate_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'start_gate_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'start_gate_complete'
            else:
                return 'start_gate_null'
        rospy.spin()

# define Path Marker 1
class path_marker_1(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['path_marker_1_complete', 'path_marker_1_null'])
        self.pub = rospy.Publisher('path_marker_1_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state path_marker_1')
        start_gate_String_pub = 'run_path_marker_1'
        self.pub.publish(path_marker_1_String_pub)
        self.sub = rospy.Subscriber("path_marker_1_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'path_marker_1_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'path_marker_1_complete'
            else:
                return 'path_marker_1_null'
        rospy.spin()

# define Bouys
class bouys(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['bouys_complete', 'bouys_null'])
        self.pub = rospy.Publisher('bouys_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state bouys')
        start_gate_String_pub = 'run_bouys'
        self.pub.publish(bouys_String_pub)
        self.sub = rospy.Subscriber("bouys_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'bouys_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'bouys_complete'
            else:
                return 'bouys_null'
        rospy.spin()
       
# define Path Marker 2
class path_marker_2(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['path_marker_2_complete', 'path_marker_2_null'])
        self.pub = rospy.Publisher('path_marker_2_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state path_marker_2')
        start_gate_String_pub = 'run_path_marker_2'
        self.pub.publish(path_marker_2_String_pub)
        self.sub = rospy.Subscriber("path_marker_2_smach_sub", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'path_marker_2_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'path_marker_2_complete'
            else:
                return 'path_marker_2_null'
        rospy.spin()

# define Channel
class channel(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['channel_complete', 'channel_null'])
        self.pub = rospy.Publisher('channel_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state path_marker_2')
        start_gate_String_pub = 'run_channel'
        self.pub.publish(channel_String_pub)
        self.sub = rospy.Subscriber("channel_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'channel_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'channel_complete'
            else:
                return 'channel_null'
        rospy.spin()
        
# define Hydrophone 1
class hydrophone_1(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['hydrophone_1_complete', 'hydrophone_1_null'])
        self.pub = rospy.Publisher('hydrophone_1_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state hydophone_1')
        start_gate_String_pub = 'run_hydophone_1'
        self.pub.publish(hydrophone_1_String_pub)
        self.sub = rospy.Subscriber("hydrophone_1_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'hydrophone_1_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'hydrophone_1_complete'
            else:
                return 'hydrophone_1_null'
        rospy.spin()

# define Dropper
class dropper(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['dropper_complete', 'dropper_null'])
        self.pub = rospy.Publisher('dropper_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state dropper')
        start_gate_String_pub = 'run_dropper'
        self.pub.publish(dropper_String_pub)
        self.sub = rospy.Subscriber("dropper_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'dropper_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'dropper_complete'
            else:
                return 'dropper_null'
        rospy.spin()

# define Torpedo
class torpedo(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['torpedo_complete', 'torpedo_null'])
        self.pub = rospy.Publisher('torpedo_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state path_marker_2')
        start_gate_String_pub = 'run_torpedo'
        self.pub.publish(torpedo_String_pub)
        self.sub = rospy.Subscriber("torpedo_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'torpedo_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'torpedo_complete'
            else:
                return 'torpedo_null'
        rospy.spin()

# define Hydrophone 2
class hydrophone_2(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['hydrophone_2_complete', 'hydrophone_2_null'])
        self.pub = rospy.Publisher('hydrophone_2_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state path_marker_2')
        start_gate_String_pub = 'run_hydrophone_2'
        self.pub.publish(hydrophone_2_String_pub)
        self.sub = rospy.Subscriber("hydrophone_2_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'hydrophone_2_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'hydrophone_2_complete'
            else:
                return 'hydrophone_2_null'
        rospy.spin()
     
# define Samples
class samples(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['samples_complete', 'samples_null'])
        self.pub = rospy.Publisher('samples_smach_transmitter', String, queue_size='10')
        rate = rospy.Rate(.5)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
        global recieved
        recieved = data.data
        rospy.loginfo('callback Display data.data: %s', recieved)
        rospy.spin()

    def execute(self, data):
        global recieved
        recieved = '0'
        rospy.loginfo('Executing state samples')
        start_gate_String_pub = 'run_samples'
        self.pub.publish(samples_String_pub)
        self.sub = rospy.Subscriber("samples_smach_receiver", String, self.callback)
        global recieved
        rospy.loginfo('execute data: %s', recieved)

        if recieved == '0':
            return 'samples_null'
            rospy.spin()
        else: 
            if recieved == '1':
                return 'samples_complete'
            else:
                return 'samples_null'
        rospy.spin()
    


def main():
    global recieved
    recieved = '0'
    rospy.init_node('sub_ai_state_manager')

    #create SMACH state machine
    sm = smach.StateMachine(outcomes=['celebrate'])

    #Open Container
    with sm:
        #add states to the Container
        smach.StateMachine.add('start_gate', start_gate(),
                            transitions={'start_gate_complete':'path_marker_1', 'start_gate_null':'start_gate'})
        smach.StateMachine.add('path_marker_1', path_marker_1(),
                            transitions={'path_marker_1_complete':'bouys', 'path_marker_1_null':'path_marker_1'})
        smach.StateMachine.add('bouys', bouys(),
							transitions={'bouys_complete':'path_marker_2', 'bouys_null':'bouys'})
        smach.StateMachine.add('path_marker_2', path_marker_2(),
							transitions={'path_marker_2_complete':'channel', 'path_marker_2_null':'path_marker_2'})
        smach.StateMachine.add('channel', channel(),
							transitions={'channel_complete':'hydrophone_1', 'channel_null':'channel'})	
        smach.StateMachine.add('hydrophone_1', hydrophone_1(),
							transitions={'hydrophone_1_complete':'dropper', 'hydrophone_1_null':'hydrophone_1'})
        smach.StateMachine.add('dropper', dropper(),
							transitions={'dropper_complete':'torpedo', 'dropper_null':'dropper'})
        smach.StateMachine.add('torpedo', torpedo(),
							transitions={'torpedo_complete':'hydrophone_2', 'torpedo_null':'torpedo'})	
        smach.StateMachine.add('hydrophone_2', hydrophone_2(),
							transitions={'hydrophone_2_complete':'samples', 'hydrophone_2_null':'hydrophone_2'})		
        smach.StateMachine.add('samples', samples(),
							transitions={'samples_complete':'celebrate', 'samples_null':'samples'})
							
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
