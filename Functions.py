#Functions
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

#Function Caching- saves time by storing already used values for a particular function
import time
from functools import lru_cache         #functools is a builtin module

@lru_cache(maxsize = 3)             #maxsize = n stores the last n values of the function call
def abc(num):
    #Function will take atleast  n seconds
    time.sleep(num)
    return num

if __name__ == '__main__':
    print("Start")
    abc(5)              #Value stored
    print("Done")
    abc(5)                  #No delay after using lru decorator
    print("Done Again")


#Passing List as Argument
def func(lis):
  for i in lis:
    print(i)
lis = [1, 2, 3]
func(lis)

#Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print(factorial(num))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))


#Local and Global Scope
'''l = 10      #Global
def fun1(n):
    #l = 5       #Local
    m = 10      #Local
    global l        #Now this function is allowed to change the value of global l
    print(l, m)
    print("Hi", n)

fun1("Nidhi")
#print(m)   local
print(l)'''

def fun2():
    x = 10
    def fun3():
        global x        #creates a global variable
        x = 20        # and sets its value to 20
    print("Before calling fun3()", x)
    fun3()
    print("After calling fun3()", x)

fun2()
print(x)