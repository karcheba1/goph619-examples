import unittest

import numpy as np

from goph619_examples.functions import exp


class TestExpValues(unittest.TestCase):

    def setUp(self):
        pass

    def test_exp_0(self):
        self.assertEqual(exp(0), 1.)


if __name__ == '__main__':
    unittest.main()
