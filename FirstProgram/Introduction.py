# Single Line Comment
"""Multi line comment"""
print("Hello World", end="")        #Won't go to next line (whatever in "" print ends with it)
print("Please Die")
print("Hello World","Please Die")       #Has space between the two statements
print("\\nidhi")        #Use \ before Escape Sequence to print them normally

#Variables
#Python chooses variable type itself
var1 = "Hello World"
var2 = 5
var3 = 23.7
var4 = " Please Die"
var5 = "52"         #string
var6 = "32"
print(type(var1))
print(type(var2))
print(type(var3))
print(var1 + var4)  #Both strings added as it is
print(var2 + var3)  #Resultant is a float
print(var1 + var5)  #Can't add a integer/float to a string variable
#Typecasting int() str() float()
print(int(var5) + int(var6))       #Converting to int
print(2 * "Hello World")           #Can't do this with int type
print(2 * str(int(var5) + int(var6)))       #Converting int to string then printing multiple times

#User Input
print("Enter a number")
num = input()       #Input is taken as a string always


