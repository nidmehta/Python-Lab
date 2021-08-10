class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}{lname}@gmail.com"

    def explain(self):
        return f"Hi {self.fname} {self.lname}"

    @property       #to take function as an attribute
    def email(self):            #setter function
        if self.fname == None or self.lname == None:
            return f"Email is not set. Please set email using setter."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting names now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

AAA = Employee("AAA", "aaa")
print(AAA.email)
print(type(AAA))
print(id(AAA))          #every object has its unique id
print(type("ssjddgcgjdcc"))
print(id("ssjddgcgjdcc"))

print(dir(AAA))         #returns all the functions/attributes that AAA has access to
s = "ssjddgcgjdcc"
print(dir(s))


import inspect
print(inspect.getmembers(AAA))