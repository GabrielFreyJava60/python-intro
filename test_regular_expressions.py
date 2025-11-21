import unittest
from regular_expressions import ipV4AddressRe, mobileIsraelNumberRe


class TestRegularExpressions(unittest.TestCase):
    
    def test_ipV4AddressRe_valid(self):
        pattern = ipV4AddressRe()
        self.assertTrue(pattern.match('192.168.1.1'))
        self.assertTrue(pattern.match('0.0.0.0'))
        self.assertTrue(pattern.match('255.255.255.255'))
        self.assertTrue(pattern.match('10.0.0.1'))
        self.assertTrue(pattern.match('172.16.0.1'))
    
    def test_ipV4AddressRe_invalid(self):
        pattern = ipV4AddressRe()
        self.assertFalse(pattern.match('256.256.256.256'))
        self.assertFalse(pattern.match('192.168.1'))
        self.assertFalse(pattern.match('192.168.1.1.1'))
        self.assertFalse(pattern.match('192.168.-1.1'))
        self.assertFalse(pattern.match('abc.def.ghi.jkl'))
        self.assertFalse(pattern.match('192.168.1.256'))
    
    def test_mobileIsraelNumberRe_valid(self):
        pattern = mobileIsraelNumberRe()
        self.assertTrue(pattern.match('0521234567'))
        self.assertTrue(pattern.match('0501234567'))
        self.assertTrue(pattern.match('0541234567'))
        self.assertTrue(pattern.match('0581234567'))
    
    def test_mobileIsraelNumberRe_invalid(self):
        pattern = mobileIsraelNumberRe()
        self.assertFalse(pattern.match('0621234567'))
        self.assertFalse(pattern.match('052123456'))
        self.assertFalse(pattern.match('05212345678'))
        self.assertFalse(pattern.match('521234567'))
        self.assertFalse(pattern.match('05-1234567'))


if __name__ == '__main__':
    unittest.main()

