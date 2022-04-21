import unittest
from unittest.case import _AssertRaisesContext
from Circle import *

import random

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Circle(100,100,5)

    def test_radius_is_positive(self):
        self.assertRaises(NegativeRadius, self.c.__init__,self.c.x,self.c.y,-1)
    def test_x_is_not_numeric(self):
        self.assertRaises(NonNumericError, self.c.__init__, "x is not a numeric value",2, 2)
    def test_y_is_not_numeric(self):
        self.assertRaises(NonNumericError, self.c.__init__,2, "y is not a numeric value",2)
    def test_r_is_not_numeric(self):
        self.assertRaises(NonNumericError, self.c.__init__,2, 2, "r is not a numeric value")

    # def test_create_circle_with_numeric_value_r(self):
    #     self.assertTrue(str(self.c.getR()).isnumeric())
    # def test_create_circle_with_numeric_value_x(self):
    #     self.assertTrue(str(self.c.getX()).isnumeric())
    # def test_create_circle_with_numeric_value_y(self):
    #     self.assertTrue(str(self.c.getY()).isnumeric())

    # def test_area_is_positive(self):
    #     self.assertGreaterEqual(self.c.getArea(), 0)
    # def test_perimeter_is_positive(self):
    #     self.assertGreaterEqual(self.c.getPerimeter(), 0)

    def test_move(self):
        for i in range(10):
            newx = random.randint(0, 100)
            newy = random.randint(0, 100)
            self.c.move(newx, newy)
            self.assertEqual(self.c.getX(), newx)
            self.assertEqual(self.c.getY(), newy)
            

if __name__ == "__main__":
	unittest.main()
# c = Circle(100,100,5)
# print(c.getR())
