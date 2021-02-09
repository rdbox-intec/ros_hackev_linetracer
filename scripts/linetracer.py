#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


class LineTracer():

    @classmethod
    def parse_cb_data(cls, data):
        return int(data[2:])

    @classmethod
    def get_init_midpoint(cls, w, b):
        return (w - b) / 2 + b

    def __init__(self):
        self.white = rospy.get_param('~white')
        self.black = rospy.get_param('~black')
        self.kp = rospy.get_param('~kp')
        self.ki = rospy.get_param('~ki')
        self.kd = rospy.get_param('~kd')
        self.td = rospy.get_param('~td')
        self.power = rospy.get_param('~power')
        # Target Value for PID
        self.midpoint = LineTracer.get_init_midpoint(self.white, self.black)
        # Internal Value
        self.__lasterror = 0.0
        self.__integral = 0.0
        # Topic Handler
        self.sub_color_sensor_reflect = rospy.Subscriber(
            'ev3rt/color_sensor_reflect',
            String,
            self.callback_color_sensor_reflect)
        self.pub_motor_steer = rospy.Publisher(
            'ev3rt/motor_steer',
            String,
            queue_size=1)

    def callback_color_sensor_reflect(self, data):
        error = self.midpoint - LineTracer.parse_cb_data(data.data)
        self.__integral = (error + self.__integral) / 2.0 * self.td
        diff = (error - self.__lasterror) / self.td
        steer = self.kp * error + self.ki * self.__integral + self.kd * diff
        int_steer = int(steer)
        self.pub_motor_steer.publish('v:{},v:{}'.format(self.power, int_steer))
        self.__lasterror = error

    def stop_all(self):
        self.pub_motor_steer.publish('v:0,v:0')


if __name__ == '__main__':
    rospy.init_node('line_tracer')

    node = LineTracer()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
