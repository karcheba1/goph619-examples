import unittest

import numpy as np

from goph619_examples.functions import exp


class TestExpValues(unittest.TestCase):

    def setUp(self):
        self.e = 2.71828182845904523536028747135266249775724709369995
        self.x_vals = np.linspace(-10., 10., 100)

    def test_exp_0(self):
        self.assertEqual(exp(0), 1.)

    def test_exp_1(self):
        expected = self.e
        self.assertAlmostEqual(exp(1), expected, delta=1.e-15)

    def test_exp_2(self):
        expected = self.e ** 2
        self.assertAlmostEqual(exp(2), expected, delta=1.e-15)

    def test_exp_array(self):
        expected = np.exp(self.x_vals)
        actual = exp(self.x_vals)
        self.assertTrue(np.allclose(actual, expected))


class TestExpString(unittest.TestCase):

    def setUp(self):
        self.e = 2.71828182845904523536028747135266249775724709369995

    def test_exp_valid_str(self):
        self.assertAlmostEqual(exp('1.0'), self.e)

    def test_exp_invalid_str(self):
        with self.assertRaises(ValueError):
            exp('zero')


class TestExpTypes(unittest.TestCase):

    def test_int_input(self):
        self.assertIsInstance(exp(1), float)

    def test_float_input(self):
        self.assertIsInstance(exp(1.0), float)

    def test_str_input(self):
        self.assertIsInstance(exp('1.0'), float)

    def test_array_input(self):
        self.assertIsInstance(exp([1, 2]), np.ndarray)


if __name__ == '__main__':
    unittest.main()
