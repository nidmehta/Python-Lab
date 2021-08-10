#from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod         #For python newer then 3.4

#if any class is inherited from abc module's ABCMeta, then it can compulsority ask its child classes to override some methods
#class Shape (metaclass = ABCMeta):
class Shape (ABC):
    @abstractmethod             #decorator
    def printArea(self):
        return 0

class Rectangle (Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.l = 6
        self.b = 8

    def printArea(self):
        return self.l * self.b

rect = Rectangle()
print(rect.printArea())

#Abstract class cannot have its own objects