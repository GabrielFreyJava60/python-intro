import unittest
from main import maxNegativeRepr


class TestMaxNegativeRepr(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, -1, -4, -100]), 100)
    
    def test_multiple_matches(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, 4, 100, -1]), 1)
    
    def test_no_match(self):
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, 4, 100, 1, -2]), -1)
    
    def test_empty_list(self):
        self.assertEqual(maxNegativeRepr([]), -1)
    
    def test_only_positive(self):
        self.assertEqual(maxNegativeRepr([1, 2, 3, 4, 5]), -1)
    
    def test_only_negative(self):
        self.assertEqual(maxNegativeRepr([-1, -2, -3, -4, -5]), -1)
    
    def test_zero_included(self):
        self.assertEqual(maxNegativeRepr([0, 1, -1, 2, -2]), 2)
    
    def test_single_pair(self):
        self.assertEqual(maxNegativeRepr([5, -5]), 5)
    
    def test_large_numbers(self):
        self.assertEqual(maxNegativeRepr([1000000, -1000000, 500, -500]), 1000000)


if __name__ == '__main__':
    unittest.main()

