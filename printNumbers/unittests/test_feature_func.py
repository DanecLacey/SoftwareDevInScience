import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from functions.feature_func import *

class TestFeatureFunc(unittest.TestCase):

    def test_value_0(self):
        self.assertEqual(does_nothing(0), 0)

    def test_value_1(self):
        self.assertEqual(does_nothing(1), 2)

    def test_value_2(self):
        self.assertEqual(does_nothing(2), 4)

    def test_value_20(self):
        self.assertEqual(does_nothing(20), 40)


def suite():
    suite = unittest.makeSuite(TestFeatureFunc, 'test')
    return suite

def run():
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())

if __name__ == "__main__":
    run()
