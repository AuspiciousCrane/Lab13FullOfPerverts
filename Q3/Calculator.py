class Error(Exception): pass
class DivideByZeroError(Error): pass
class NonNumericError(Error): pass

"""
class Calculator:
	def __init__(self):
		self.acc = 0.00

	def set_accumulator(self, a):
		if not (isinstance(a, int) or isinstance(a, float)):
			raise NonNumericError("Input is not a number")
		self.acc = a

	def get_accumulator(self):
		return self.acc

	def add(self, x):
		if not (isinstance(x, int) or isinstance(x, float)):
			raise NonNumericError("Input is not a number")
		self.acc += x

	def subtract(self, x):
		if not (isinstance(x, int) or isinstance(x, float)):
			raise NonNumericError("Input is not a number")
		self.acc -= x

	def multiply(self, x):
		if not (isinstance(x, int) or isinstance(x, float)):
			raise NonNumericError("Input is not a number")
		self.acc *= x

	def divide(self, x):
		if not (isinstance(x, int) or isinstance(x, float)):
			raise NonNumericError("Input is not a number")

		if x == 0:
			raise DivideByZeroError("You cannot divide a number by zero")

		self.acc /= x

	def get_status(self):
		return f"Result: {self.acc}"

if __name__ == "__main__":
	c = Calculator()
	print(isinstance(c.acc, float))
	print(c.get_status())
"""
