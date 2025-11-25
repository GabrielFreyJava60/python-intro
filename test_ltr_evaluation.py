from unittest import TestCase
from ltr_evaluation import ltrEvaluation, _checkArithmeticExpr


class TestLtrEvaluation(TestCase):
    
    def test_ltr_eval(self):
        expr = "(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10"
        self.assertAlmostEqual(160.0, ltrEvaluation(expr), places=1)
        expr = "((3.5 + (2 * 10.45 / (40.5 - 40))+(3 * 4)) * (10.2 ** 2)) / 2.55"
        self.assertAlmostEqual(
            ((3.5 + (2 * 10.45 / (40.5 - 40))+(3 * 4)) * (10.2 ** 2)) / 2.55,
            ltrEvaluation(expr),
            places=1
        )
        with self.assertRaises(ValueError):
            ltrEvaluation("4 + 2   5")
        with self.assertRaises(ZeroDivisionError):
            ltrEvaluation("4 + 2  / (20 / 20 - 1)")


class TestCheckArithmeticExpr(TestCase):
    
    def test_valid_expression(self):
        is_valid, msg = _checkArithmeticExpr("(10 + 20) * 5")
        self.assertTrue(is_valid)
        self.assertEqual(msg, "valid")
    
    def test_valid_with_pow(self):
        is_valid, msg = _checkArithmeticExpr("2 ** 3 + 5")
        self.assertTrue(is_valid)
        self.assertEqual(msg, "valid")
    
    def test_syntax_error(self):
        is_valid, msg = _checkArithmeticExpr("10 + + 20")
        self.assertFalse(is_valid)
        self.assertIn("syntax error", msg)
    
    def test_pairing_error_extra_closing(self):
        is_valid, msg = _checkArithmeticExpr("(10 + 20))))")
        self.assertFalse(is_valid)
        self.assertIn("parentheses pairing error", msg)
    
    def test_pairing_error_extra_opening(self):
        is_valid, msg = _checkArithmeticExpr("((((10 + 20)")
        self.assertFalse(is_valid)
        self.assertIn("parentheses pairing error", msg)
    
    def test_syntax_ok_pairing_ok(self):
        is_valid, msg = _checkArithmeticExpr("(10 + 20) / (5 * 2)")
        self.assertTrue(is_valid)
        self.assertEqual(msg, "valid")
    
    def test_both_errors(self):
        is_valid, msg = _checkArithmeticExpr("(10 + + 20))))")
        self.assertFalse(is_valid)
        self.assertIn("syntax error", msg)
        self.assertIn("parentheses pairing error", msg)
    
    def test_nested_parentheses(self):
        is_valid, msg = _checkArithmeticExpr("((10 + 5) * (20 - 3))")
        self.assertTrue(is_valid)
        self.assertEqual(msg, "valid")
    
    def test_float_numbers(self):
        is_valid, msg = _checkArithmeticExpr("3.14 + 2.71 * 1.41")
        self.assertTrue(is_valid)
        self.assertEqual(msg, "valid")
