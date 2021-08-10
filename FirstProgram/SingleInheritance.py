class Employee:
    year = 2020

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.year = 2021        #Instance variable

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

class Coder(Employee):
    def __init__(self, name, age, languages):
        super().__init__(name, age)
        self.languages = languages

    def printDet(self):
        return f"Hi {self.name}, your age is {self.age} and you know {self.languages}"

AAA = Employee("AAA", 20)
BBB = Coder("BBB", 18, ["Cpp", "Python"])          #Has all the members of both classes
print(BBB.printDet())

#If any variable call happens then first interpreter searches for instance variable in derived class, then for instance variable in base class, next class variable in derived class and astly class variable in base class