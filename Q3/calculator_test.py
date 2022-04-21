import unittest
import random
from Calculator import Calculator, DivideByZeroError

class CalculatorTest(unittest.TestCase):
	def setUp(self):
		self.calc = Calculator()
		random.seed(69420)

	def testNewCalculator(self):
		self.assertEqual(0.00, self.calc.get_accumulator())
		self.assertTrue(isinstance(self.calc.get_accumulator(), float))

	def testDivideByZero(self):
		self.assertRaises(DivideByZeroError, self.calc.divide, 0)

	def testSetGetAccumulator(self):
		acc_value = random.uniform(-69420, 69420)
		self.calc.set_accumulator(acc_value)

		self.assertEqual(self.calc.get_accumulator(), acc_value)

"""
	def testAdd(self):
		for i in range(420):
			init_value = random.uniform(-69420, 69420)
			value_to_add = random.uniform(-69420, 69420)

			self.calc.set_accumulator(init_value)
			self.calc.add(value_to_add)

			self.assertEqual(self.calc.get_accumulator(), init_value + value_to_add)

	def testSubtract(self):
		for i in range(420):
			init_value = random.uniform(-69420, 69420)
			value_to_subtract = random.uniform(-69420, 69420)

			self.calc.set_accumulator(init_value)
			self.calc.subtract(value_to_subtract)

			self.assertEqual(self.calc.get_accumulator(), init_value - value_to_subtract)

	def testMultiply(self):
		for i in range(420):
			init_value = random.uniform(-69420, 69420)
			value_to_multiply = random.uniform(-69420, 69420)

			self.calc.set_accumulator(init_value)
			self.calc.multiply(value_to_multiply)

			self.assertEqual(self.calc.get_accumulator(), init_value * value_to_multiply)

	def testDivide(self):
		for i in range(420):
			init_value = random.uniform(-69420, 69420)
			value_to_divide = random.uniform(-69420, 69420)

			while (value_to_divide) == 0:
				value_to_divide = random.uniform(-69420, 69420)

			self.calc.set_accumulator(init_value)
			self.calc.divide(value_to_divide)

			self.assertEqual(self.calc.get_accumulator(), init_value / value_to_divide)

	def testGetStatus(self):
		for i in range(420):
			init_value = random.uniform(-69420, 69420)

			self.calc.set_accumulator(init_value)
			self.assertEqual(self.calc.get_status(), f"Result: {init_value}")
"""

if __name__ == "__main__":
	unittest.main()
