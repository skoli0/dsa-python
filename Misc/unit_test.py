# Python code to demonstrate working of unittest 
import unittest 

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci (n - 1)

class TestFibonacciMethod(unittest.TestCase): 
    def test_fibonacci__nth(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)
	
if __name__ == '__main__': 
	unittest.main() 
