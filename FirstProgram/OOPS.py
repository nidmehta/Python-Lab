#Classes- Templates
#Objects- Instance of Class
#Concept- DRY Dont Repeat Yourself

#class Student:
#    pass
#Nid = Student()
#Dhi = Student()
#print(Nid, Dhi)
#Nid.name = "Nidhi"
#print(Nid.name)


class Employee:
    year = 2020         #same/common for all objects of a class

    def __init__(self, aname, aage):        #Constructor
        self.name = aname
        self.age = aage

    def printDetails(self):         #self refers to currently calling object
        return f"Hi {self.name}, your age is {self.age}"

    @classmethod            #decorator
    def change_year(cls, newyear):          #cls refers to the current class
        cls.year = newyear

    #class method as a constructor
    @classmethod
    def from_dash(cls, string):
        #params = string.split("-")         #params forms a list, split splits the string
        #return cls(params[0], params[1])
        #OR
        return cls(*string.split("-"))

    #Static method- does not take cls or self as an argument
    @staticmethod           #reduces time by eliinating extra arguments
    def printHello(string):
        print("Hello", string)
        return "Done"       #if there is no return statement then None is returned by default

#AAA = Employee()
#BBB = Employee()

#AAA.name = "AAA"
#AAA.age = 18

#BBB.name = "BBB"
#BBB.age = 20

#class variable can be accessed/shared by all the objects of class and the class itself but can be change only by the class
#print(AAA.year)
#print(BBB.year)
#print(Employee.year)

#Employee.year = 2021
#print(Employee.year)

#AAA.year = 2024
#print(Employee.year)        #Doesnt change

#print(AAA.__dict__)         #Returns a dictionary of all the attributes of the particular object

#print(AAA.printDetails())
#print(BBB.printDetails())

#CCC = Employee("CCC", 19)
#print(CCC.printDetails())

DDD = Employee.from_dash("DDD-22")
#print(DDD.printDetails())
print(DDD.printHello("DDD"))

