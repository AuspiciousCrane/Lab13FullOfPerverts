import unittest

class StackError(Exception): pass
class OutOfRangeError(StackError): pass

class Stack:
    def __init__(self):
        self.__sList = []

    def push(self, inElement):
        self.__sList.append(inElement)
    
    def pop(self):
        if len(self.__sList) <= 0:
            raise OutOfRangeError("Cannot pop empty list")
        else:
            return self.__sList.pop()

    def isEmpty(self):
        return len(self.__sList) == 0
    
    def size(self):
        return len(self.__sList)
    
    def peek(self):
        if len(self.__sList) <= 0:
            raise OutOfRangeError("Cannot peek empty list")
        else:
            return self.__sList[-1]

class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def testNewStack(self):                # (1)
        """
        A stack is empty on construction and its size is obviously zero
        """
        self.assertTrue(self.s.isEmpty())
        self.assertEquals(self.s.size(), 0)

    def testPushes(self):                  # (2)
        """
        After n pushes (where n > 0) to an empty stack, the stack is not empty and its size is n
        """
        nPushes = 6
        for i in range(nPushes):
            self.s.push("item")

        self.assertFalse(self.s.isEmpty())
        self.assertEqual(self.s.size(), nPushes)

    def testPushPop(self):                 # (3)
        """
        If one pushes x then pops, the value popped is x
        """
        size = self.s.size()

        item = "Python"
        self.s.push(item)
        self.assertEqual(self.s.pop(), item)
        self.assertEqual(self.s.size(), size)

    def testPeek(self):
        """
        If one pushes x then peeks, the value returned is x but the size stays the same
        """
        item1 = "apple"
        item2 = "banana"

        self.s.push(item1)
        self.s.push(item2)

        size = self.s.size()
        
        self.assertEqual(self.s.peek(), item2)
        self.assertEqual(self.s.size(), size)

    # def testPopAll(self):
    #     """
    #     If the size is n(where n > 0), then after n pops, the stack is empty
    #     """
    #     n = 6
    #     for _ in range(n):
    #         self.s.push("item")
        
    #     for _ in range(n):
    #         self.s.pop()
        
    #     self.assertTrue(self.s.isEmpty())

    # def testPeekEmptyStack(self):
    #     """
    #     Popping from an empty stack will raise OutOfRangeError
    #     """
    #     self.assertRaises(OutOfRangeError, self.s.peek)

    # def testPopEmptyStack(self):
    #     """
    #     Peeking into empty stack will raise OutOfRangeError
    #     """
    #     self.assertRaises(OutOfRangeError, self.s.pop)


def suite():
	suite = unittest.TestSuite()
	suite.addTest(StackTest("testNewStack"))
	suite.addTest(StackTest("testPushes"))
	return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(StackTest("testPeekEmptyStack"))
    suite.addTest(StackTest("testPopEmptyStack"))
    return suite

if __name__ == "__main__":
	#unittest.main(verbosity=2)
    unittest.TextTestRunner(verbosity=2).run(suite())
    unittest.TextTestRunner(verbosity=2).run(suite2())
	#unittest.TextTestRunner().run(suite())
