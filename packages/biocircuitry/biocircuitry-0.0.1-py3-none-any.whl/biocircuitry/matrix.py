import numpy as np
from .abstractClasses import BaseArrayNP

class MatrixNP(BaseArrayNP):
    def __init__(self, matrix, _dtype = np.int8):
        self.dtype = _dtype
        self.matrix = matrix
    
    def transform2NP(self, matrix):
        return np.array([matrix[idx].arr.tolist() for idx in range(len(matrix))], dtype=self.dtype)
        
    def operations(self, other, operation):
        try:
            _matrixLength = len(other.matrix)
            #exec(f'tmp = [[{self.matrix[idx].arr[idy]} {operation} {other.matrix[idx].arr[idy]} for idy in range(len({self.matrix[0].arr}))]')# for idx in range(len({self.matrix}))]')
            #return tmp
            if operation == "+":
                return [[self.matrix[idx].arr[idy] + other.matrix[idx].arr[idy] for idy in range(len(self.matrix[0].arr))] for idx in range(len(self.matrix))] 
            elif operation == "-":
                return [[self.matrix[idx].arr[idy] - other.matrix[idx].arr[idy] for idy in range(len(self.matrix[0].arr))] for idx in range(len(self.matrix))] 
            elif operation == "/":
                return [[self.matrix[idx].arr[idy] / other.matrix[idx].arr[idy] for idy in range(len(self.matrix[0].arr))] for idx in range(len(self.matrix))] 
            elif operation == "**":
                return [[self.matrix[idx].arr[idy] ** other.matrix[idx].arr[idy] for idy in range(len(self.matrix[0].arr))] for idx in range(len(self.matrix))] 
            else:
                A = np.transpose(self.transform2NP(self.matrix))
                B = np.array(self.transform2NP(other.matrix))
                return np.matmul(A, B).tolist()
        except:
            if operation != "**":
                exec(f'tmp = [[self.matrix[idx].arr[idy] {operation} other for idy in range(len(self.matrix[0].arr))] for idx in range(len(self.matrix))]')
            return tmp
        
    def __add__(self, other):
        return self.operations(other, "+")
    
    def __sub__(self, other):
        return self.operations(other, "-")
    
    def __mul__(self, other):
        return self.operations(other, "*")
    
    def __div__(self, other):
        return self.operations(other, "/")
    
    def __pow__(self, other):
        return self.operations(other, "**")
      
    def shape(self):
        return (len(self.matrix), len(self.matrix[0]))
    
    def concat(self, other, _axis = 0):
        return np.concatenate((self.transform2NP(self.matrix), self.transform2NP(other.matrix)), axis=_axis)
        
    def mean(self, _axis = 1):
        return np.mean(self.transform2NP(self.matrix), axis=_axis)
    
    def variance(self, _axis = 0):
        return np.var(self.transform2NP(self.matrix), axis=_axis)
    
    def standardDeviation(self, _axis = None):
        return np.std(self.transform2NP(self.matrix), axis=_axis)
    
    def innerProduct(self, other):
        return np.inner(self.transform2NP(self.matrix), self.transform2NP(other.matrix))
    
    def outerProduct(self, other):
        return np.outer(self.transform2NP(self.matrix), self.transform2NP(other.matrix))
    
    def dot(self, other):
        return np.dot(self.transform2NP(self.matrix), self.transform2NP(other.matrix))
    
    def cross(self, other):
        return np.cross(self.transform2NP(self.matrix), self.transform2NP(other.matrix))
    
    def getLambdify(self, formula, variable):
        return sp.lambdify(variable, formula, "numpy")
    
    def applyFunction(self, formula, variable):
        functionSP = self.getLambdify(formula, variable)
        return functionSP(self.transform2NP(self.matrix))
    
    def norm(self, root = 2):
        return np.power(np.sum(self.transform2NP(self.matrix)), 1 / root)
    
    def rms(self, root = 2):
        x, y = self.shape()
        return self.norm(root=root) / np.sqrt(x * y)
