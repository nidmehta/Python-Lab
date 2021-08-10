#Methods whose name starts and ends with '__' are dunder methods
class Employee:
    year = 2020

    def __init__(self, name, age):          #dunder method
        self.name = name
        self.age = age
        self.year = 2021

    def printDetails(self):
        return f"Hi {self.name}, your age is {self.age}"

    @classmethod
    def change_year(cls, newyear):
        cls.year = newyear

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printHello(string):
        print("Hello", string)
        return "Done"

    #Search mapping operators to functions
    def __add__(self, other):               #dunder method helps in operator overloading
        return self.age + other.age

    def __repr__(self):
        return f"Employee('{self.name}',{self.age})"

    def __str__(self):
        return f"Hi {self.name}, your age is {self.age}"

AAA = Employee("AAA", 20)
BBB = Employee("BBB", 21)
print(AAA + BBB)                #searches for a dunder function to overload operator
print(AAA)                      #searches for __repr__ if __str__ is not there. Always gives priority to str dunder function
print(str(AAA))                 #If str is not there then it will go for repr
print(repr(AAA))                #To specifically call repr function