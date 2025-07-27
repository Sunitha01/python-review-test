"""
Tests for calculator module
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test calculator"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_history(self):
        """Test calculation history"""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("1 + 2 = 3", history)
        self.assertIn("3 * 4 = 12", history)

if __name__ == "__main__":
    unittest.main()