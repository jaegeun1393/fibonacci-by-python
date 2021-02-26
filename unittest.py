import unittest

def fibonacci(n):
	return 1 if n<=2 else fibonacci(n-1)+fibonacci(n-2)

class TestFibonacci(unittest.TestCase):

	def test_fibonacci(self):
		self.assertEqual(fibonacci(66),66)

	def test_fibonacci_true(self):
		self.assertTrue(fibonacci(66)==66)

if __name__ == '__main__':
	unittest.main()
