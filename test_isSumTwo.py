import unittest
from main import isSumTwo


class TestIsSumTwo(unittest.TestCase):
    
    def test_sum_exists(self):
        self.assertTrue(isSumTwo([1, 2, 3, 4], 4))
    
    def test_sum_does_not_exist(self):
        self.assertFalse(isSumTwo([1, 2, 3, 4], 2))
    
    def test_empty_list(self):
        self.assertFalse(isSumTwo([], 5))
    
    def test_single_element(self):
        self.assertFalse(isSumTwo([5], 5))
    
    def test_negative_numbers(self):
        self.assertTrue(isSumTwo([-1, 2, 3, -2], 1))
    
    def test_zero_sum(self):
        self.assertTrue(isSumTwo([-5, 0, 5], 0))
    
    def test_large_numbers(self):
        self.assertTrue(isSumTwo([1000000, 2000000, 3000000], 5000000))
    
    def test_duplicates(self):
        self.assertTrue(isSumTwo([2, 2, 3], 4))


if __name__ == '__main__':
    unittest.main()

