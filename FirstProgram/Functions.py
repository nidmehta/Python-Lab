#Inbuilt Functions
a = 1
b = 2
c = sum((a, b))
print(c)

#User Defined Functions
def func1(a, b):
    print("Function 1: Sum =", a+b)
func1(1, 2)

#Docstrings- the first line inside a function specified between """ """
def func2(c, d):
    """Function to print average of two numbers"""
    avg = (c+d)/2
    return avg
v = func2(5, 7)
print(v)
print(func2.__doc__)
