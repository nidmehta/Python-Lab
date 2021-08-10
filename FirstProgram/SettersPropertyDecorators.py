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

print(AAA.explain())
print(AAA.email)

AAA.fname = "CoolAAA"
#print(AAA.email)        #Does not change as the constructor is only run when the object was created and not after that

#print(AAA.email())     #when property decorator was not there

print(AAA.email)        #after using property decorator

#We cannot directly set email as it is made from other attributes (fname, lname), hence we use setter which also changes the attributes which our original attribute is made up of
AAA.email = "aaa.AAA@gmail.com"
print(AAA.fname)
print(AAA.lname)
print(AAA.email)

#Can't delete attribute directly so we need a deleter
del AAA.email
print(AAA.fname)
print(AAA.lname)
print(AAA.email)        #Show None.None@gmail.com without the if condition in property decorator

AAA.email = "QWE.ASD@gmail.com"         #Setting email using setter again
print(AAA.email)