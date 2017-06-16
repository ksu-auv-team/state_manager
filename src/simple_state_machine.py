#!/usr/bin/env python

import roslib; #roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
from std_msgs.msg import String

# define state Foo
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])
        self.counter = 0
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
        rate = rospy.Rate(10)

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        hello_str = "state Foo %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        self.pub.publish(hello_str)

        if self.counter < 30000000000:
            self.counter += 1
            return 'outcome1'
        else:
            return 'outcome2'


# define state Bar
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        self.pub = rospy.Publisher('chatter2', String, queue_size=10)
        rate = rospy.Rate(10)

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        bar_str = "state Bar"
        rospy.loginfo(bar_str)
        self.pub.publish(bar_str)
        return 'outcome1'
        




def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome4'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('FOO', Foo(), 
                               transitions={'outcome1':'BAR', 'outcome2':'outcome4'})
        smach.StateMachine.add('BAR', Bar(), 
                               transitions={'outcome1':'FOO'})

    # Execute SMACH plan
    #outcome = sm.execute()
    
    sis = smach_ros.IntrospectionServer('smach_server', sm, '/SM_ROOT')
    sis.start()
    sm.execute()
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
