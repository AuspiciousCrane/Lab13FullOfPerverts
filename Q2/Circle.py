from cmath import pi
from re import X

class Error(Exception): pass
class NonNumericError(Error): pass
class NegativeRadius(Error): pass

class Circle():
    def __init__(self, x, y, r):
        if not (isinstance(x, int) or isinstance(y, int) or isinstance(r, int) or isinstance(x, float) or isinstance(y, float) or isinstance(r, float)):
            raise NonNumericError
        self.x = x
        self.y = y
        if(r < 0):
            raise NegativeRadius
        self.r = r
    def getArea(self):
        return pi*self.r**2
    def getPerimeter(self):
        return 2*pi*self.r
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getR(self):
        return self.r

c = Circle("asd", 100, 5)
print(c.getArea)
	

# What need to be test
## x must be a number
## y must be a number
## r must be a number
## r should not be an negative number
## getting an negative circumference raises an error
## getting an negative area raises an error
## the value of x and y should be equal to the value newx and newy respectively