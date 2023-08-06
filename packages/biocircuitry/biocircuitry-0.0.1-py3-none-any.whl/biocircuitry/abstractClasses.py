from abc import ABC, abstractmethod

class BaseArrayNP:
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
    
    def dimensions(self, arr):
        return arr.shape
    
    def typeID(self, arr):
        return arr.dtype
    
    @abstractmethod
    def __mul__(self, other):
        pass
    
    @abstractmethod
    def __sub__(self, other):
        pass
    
    @abstractmethod
    def __add__(self, other):
        pass
    
    @abstractmethod
    def concat(self, other):
        pass
