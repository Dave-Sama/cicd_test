# tests/test_my_code.py

import unittest
from src.my_code import add_numbers

class TestMyCode(unittest.TestCase):
    def test_add_numbers(self):
        """
        Test the add_numbers function with sample inputs.
        """
        
        # Succeeded test cases
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        
        # Failed test case
        #self.assertEqual(add_numbers(0, 0), 1)

if __name__ == "__main__":
    unittest.main()
