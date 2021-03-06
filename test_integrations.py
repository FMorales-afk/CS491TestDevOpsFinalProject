import unittest 
import calculator 

class TestCalculator(unittest.TestCase):

    def test_add_subtract(self):
     self.assertEqual(calculator.add(4,7), 11)
     self.assertEqual(calculator.subtract(10,5), 5)

    def test_multiply_divide(self):
     self.assertEqual(calculator.multiply(3,7), 21)
     self.assertEqual(calculator.divide(100,2), 50)

    def test_multiply_subtract(self):
      self.assertEqual(calculator.multiply(3,7), 21)
      self.assertEqual(calculator.subtract(10,5), 5)
   
    def test_divide_add(self):
     self.assertEqual(calculator.divide(100,2), 50)
     self.assertEqual(calculator.add(4,7), 11)

if __name__ == "__main__":
        unittest.main()
