import unittest
import operations

class TestOperations(unittest.TestCase):

    def test_add(self):
        result= operations.add(2,3)
        self.assertEqual(result,5,"Wrong add result")
    
    def test_subtract(self):
        result= operations.subtract(5,3)
        self.assertEqual(result,2,"Wrong subtract result")
        
    def test_multiply(self):
        result= operations.multiply(3,2)
        self.assertEqual(result,6,"Wrong multiply result")
        
    def test_divide(self):
        result= operations.divide(9,3)
        self.assertEqual(result,3,"Wrong divide result")
    
if __name__ == '__main__':
    unittest.main()
