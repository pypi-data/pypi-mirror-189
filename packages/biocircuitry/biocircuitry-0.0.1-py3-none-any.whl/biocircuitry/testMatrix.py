import unittest
from .matrix import MatrixNP
from .vector import VectorNP

class TestMatrixNP(unittest.TestCase):
    def setUp(self):
        self.A = MatrixNP([VectorNP(2, [0,4]),VectorNP(2, [7,0]),VectorNP(2, [3,1])])
        self.B = MatrixNP([VectorNP(2, [1,2]),VectorNP(2,[2,3]),VectorNP(2, [0,4])])
    
    def test_add(self):
        self.assertEqual(self.A + self.B, [[1,6],[9,3],[3,5]], "Adding")
    
    def test_sub(self):
        self.assertEqual(self.A - self.B, [[-1, 2], [5, -3], [3, -3]], "Subtraction")
        
    def test_mul(self):
        self.assertEqual(self.A * self.B, [[14, 33], [4, 12]], "Multiplication")
    
    def test_pow(self):
        self.assertEqual(self.A ** self.B, [[0, 16], [49, 0], [1, 1]], "Power")
        
    def test_norm(self):
        self.assertEqual(round(self.A.norm()), 4, "Norm close to 4")
        
    def test_rms(self):
        self.assertEqual(round(self.A.rms()), 2, "RMS close to 2")
