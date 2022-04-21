from cmath import pi

class Error(Exception): pass
class NonNumericError(Error): pass
class NegativeRadius(Error): pass

class Circle():
    def __init__(self, x, y, r):
        if not (isinstance(x, int) or isinstance(x, float)):
            raise NonNumericError("X is not a number")
        if not (isinstance(y, int) or isinstance(y, float)):
            raise NonNumericError("Y is not a number")
        if not (isinstance(r, int) or isinstance(r, float)):
            raise NonNumericError("r is not a number")

        self.x = x
        self.y = y

        if(r < 0):
            raise NegativeRadius

        self.r = r
    def getArea(self):
        return pi*self.r * self.r
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

# What need to be test
## x must be a number
## y must be a number
## r must be a number
## r should not be an negative number
## getting an negative circumference raises an error
## getting an negative area raises an error
## the value of x and y should be equal to the value newx and newy respectively
