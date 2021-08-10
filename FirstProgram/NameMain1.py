#Import automatically executes whatever file is imported to avoid that unwanted execution we use main

def printName(string):
    return f"My name is {string}"           #using f string

def addNum(n1, n2):
    return n1 + n2 + 10

print("__name__ is ", __name__) #name is main when the program in which main is there is executed
if __name__ == '__main__':
    print(printName("Nidhi"))
    a = addNum(6, 8)
    print(a)