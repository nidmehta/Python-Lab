#Conditionals
var1 = 6
var2 = 56
var3 = int(input())
if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

list1 = [1, 2, 3, 4, 5]
print(5 in list1)
print(5 not in list1)
if 4 in list1:
    print("Yes")


#Loops
list2 = [["M", 1], ["N",2], ["G",3], ["T", 4]]
for item, number in list2:                  #list, tuples, list of list can be iterated like this
    print(item, number)
dict1 = dict(list2)                         #printing using dict
for item, number in dict1.items():
    print(item, "-", number)

i = 0
while(i < 5):
    print(i)
    i = i + 1

while(True):
    num = int(input())
    if num > 100:
        print("Break")
        break
    else:
        print("Continue")
        continue
