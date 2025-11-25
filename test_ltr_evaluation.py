from unittest import TestCase
from ltr_evaluation import ltr_evaluation, _check_arithmetic_expr, ErrorMessages


class TestLtrEvaluation(TestCase):
    
    def test_basic_expression(self):
        expr = "(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10"
        self.assertAlmostEqual(160.0, ltr_evaluation(expr), places=1)
    
    def test_float_expression(self):
        expr = "((3.5 + (2 * 10.45 / (40.5 - 40))+(3 * 4)) * (10.2 ** 2)) / 2.55"
        expected = ((3.5 + (2 * 10.45 / (40.5 - 40))+(3 * 4)) * (10.2 ** 2)) / 2.55
        self.assertAlmostEqual(expected, ltr_evaluation(expr), places=1)
    
    def test_syntax_error_raises_value_error(self):
        with self.assertRaises(ValueError):
            ltr_evaluation("4 + 2   5")
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            ltr_evaluation("4 + 2  / (20 / 20 - 1)")


class TestCheckArithmeticExpr(TestCase):
    
    def test_valid_expression(self):
        is_valid, msg = _check_arithmetic_expr("(10 + 20) * 5")
        self.assertTrue(is_valid)
        self.assertEqual(msg, ErrorMessages.VALID)
    
    def test_valid_with_pow(self):
        is_valid, msg = _check_arithmetic_expr("2 ** 3 + 5")
        self.assertTrue(is_valid)
        self.assertEqual(msg, ErrorMessages.VALID)
    
    def test_syntax_error_double_operator(self):
        is_valid, msg = _check_arithmetic_expr("10 + + 20")
        self.assertFalse(is_valid)
        self.assertEqual(msg, ErrorMessages.SYNTAX_ERROR)
    
    def test_pairing_error_extra_closing(self):
        is_valid, msg = _check_arithmetic_expr("(10 + 20))))")
        self.assertFalse(is_valid)
        self.assertEqual(msg, ErrorMessages.PAIRING_ERROR)
    
    def test_pairing_error_extra_opening(self):
        is_valid, msg = _check_arithmetic_expr("((((10 + 20)")
        self.assertFalse(is_valid)
        self.assertEqual(msg, ErrorMessages.PAIRING_ERROR)
    
    def test_valid_complex_expression(self):
        is_valid, msg = _check_arithmetic_expr("(10 + 20) / (5 * 2)")
        self.assertTrue(is_valid)
        self.assertEqual(msg, ErrorMessages.VALID)
    
    def test_both_syntax_and_pairing_errors(self):
        is_valid, msg = _check_arithmetic_expr("(10 + + 20))))")
        self.assertFalse(is_valid)
        self.assertEqual(msg, ErrorMessages.BOTH_ERRORS)
    
    def test_nested_parentheses(self):
        is_valid, msg = _check_arithmetic_expr("((10 + 5) * (20 - 3))")
        self.assertTrue(is_valid)
        self.assertEqual(msg, ErrorMessages.VALID)
    
    def test_float_numbers(self):
        is_valid, msg = _check_arithmetic_expr("3.14 + 2.71 * 1.41")
        self.assertTrue(is_valid)
        self.assertEqual(msg, ErrorMessages.VALID)
    
    def test_adjacent_digits_is_syntax_error(self):
        is_valid, msg = _check_arithmetic_expr("4 + 2   5")
        self.assertFalse(is_valid)
        self.assertEqual(msg, ErrorMessages.SYNTAX_ERROR)
