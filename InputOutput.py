#Input from the user
name = input("Enter Your Name: ")

#Output
print("Hello, " + name)

#Input using split function
print("Enter Two Numbers: ")
x, y = map(int, input().split())
print("Sum: ", x + y)

#F Strings and String Formatting
import math

me = "Nidhi"
a = "Hi %s"%me
print(a)
age = 20
a = "Hi %s %s"%(me, age)
print(a)

a = "Hi {} {}"
b = a.format(me, age)
print(b)
a = "Hi {1} {0}"
b = a.format(me, age)
print(b)

a = f"Hi {me} {age} {4*4} {math.cos(0)}"
print(a)

