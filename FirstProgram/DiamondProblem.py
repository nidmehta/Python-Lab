#No ambiguity in python due to multiple inheritance
class A:
    def printMethod(self):
        print("Class A")

class B (A):
    def printMethod(self):
        print("Class B")

class C (A):
    def printMethod(self):
        print("Class C")

class D (B, C):
    def printMethod(self):
        print("Class D")

a = A()
b = B()
c = C()
d = D()

d.printMethod()