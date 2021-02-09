#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('ev3rt/color_sensor_reflect', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(30)
    while not rospy.is_shutdown():
        str = "v:50"
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
