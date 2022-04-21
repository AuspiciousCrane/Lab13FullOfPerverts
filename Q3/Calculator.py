class Error(Exception): pass
class DivideByZeroError(Error): pass

"""
class Calculator:
	def __init__(self):
		self.acc = 0.00

	def set_accumulator(self, a):
		self.acc = a

	def get_accumulator(self):
		return self.acc

	def add(self, x):
		self.acc += x

	def subtract(self, x):
		self.acc -= x

	def multiply(self, x):
		self.acc *= x

	def divide(self, x):
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
