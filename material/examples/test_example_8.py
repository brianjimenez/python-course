from nose.tools import assert_almost_equals
import math


class Circle(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


class TestCircle:

    def setUp(self):
        self.c = Circle(0., 0., 3.)

    def tearDown(self):
        pass

    def test_area(self):
        assert_almost_equals(28.27433388, self.c.area())
