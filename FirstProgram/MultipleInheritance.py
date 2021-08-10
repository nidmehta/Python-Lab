class Employee:
    year = 2020

    def __init__(self, name, age):
        self.name = name
        self.age = age

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

class Player:
    games = 5

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDet(self):
        return f"Hi {self.name}, you play {self.age}"

class CoolPeeps(Employee, Player):          #Order matters
    pass

AAA = Employee("AAA", 20)
BBB = Player("BBB", ["Cricket"])
#CCC = CoolPeeps()