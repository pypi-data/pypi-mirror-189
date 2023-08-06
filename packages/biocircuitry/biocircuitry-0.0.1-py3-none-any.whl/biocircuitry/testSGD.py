import unittest
from .sgd import SGD_NP
from sympy import *
import numpy as np
from .vector import VectorNP

class TestSGD_NP(unittest.TestCase):
    def setUp(self):
        v = symbols("v")
        equation = v**2
        array = np.array(VectorNP(10, [10] * 10, _dtype=np.float64).arr.tolist(), dtype=np.float64)
        learningRate = 0.2

        self.sgd = SGD_NP(array, equation, [v], learningRate)
        
    def test_start(self):
        self.assertEqual(self.sgd.start(display=False)[0], 2.210739197207331e-06, "Testing SGD")
