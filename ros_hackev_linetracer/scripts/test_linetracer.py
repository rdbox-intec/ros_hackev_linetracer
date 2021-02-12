#!/usr/bin/env python

import unittest
import rostest
from linetracer import LineTracer


class Test_LineTracer(unittest.TestCase):

    def test_get_init_midpoint(self):
        self.assertEqual(50, LineTracer.get_init_midpoint(80, 20))
        self.assertEqual(55, LineTracer.get_init_midpoint(100, 10))
        self.assertEqual(44.5, LineTracer.get_init_midpoint(67, 22))

    def test_parse_cb_data(self):
        self.assertEqual(10, LineTracer.parse_cb_data('v:10'))
        self.assertEqual(0, LineTracer.parse_cb_data('v:0'))
        self.assertEqual(100, LineTracer.parse_cb_data('v:100'))


if __name__ == '__main__':
    rostest.rosrun("ros_hackev_linetracer", 'test_all', Test_LineTracer)
