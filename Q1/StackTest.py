import unittest

class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def testNewStack(self):                # (1)
        self.assertTrue(self.s.isEmpty())
        self.assertEqual(self.s.size(), 0)

    def testPushes(self):                  # (2)
        nPushes = 6
        for i in range(nPushes):
            self.s.push("item")

        self.assertFalse(self.s.isEmpty())
        self.assertEquals(self.s.size(), nPushes)

    def testPushPop(self):                 # (3)
        size = self.s.size()

        item = "Python"
        self.s.push(item)
        self.assertEqual(self.s.pop(), item)
        self.assertEqual(self.s.size(), size)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(StackTest("testNewStack")
	suite.addTest(StackTest("testPushes")
	return suite

if __name__ == "__main__":
	#unittest.main()
	unittest.TextTestRunner().run(suite())
