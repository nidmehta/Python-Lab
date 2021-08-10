#Lists - mutable
name = ["Nidhi", "John", "Joe", "Harry", "Ron", "Draco", 88]
print(name)
print(name[4])

num = [1, 4, 5, 3, 2]
print(num)
print(num[4])
num.sort()          #changes the original list
print(num)
num.reverse()       #changes the original list
print(num)
print(num[0:5])
print(num[:5])
print(num[0:5])
print(num[:])
print(num[::-1])       #reverses the list
print(len(num))
print(max(num))
print(min(num))
num.append(6)       #inserts at end only
print(num)
num.insert(3, 7)    #insert(at index, value)
print(num)
num.remove(7)       #remove(value)
print(num)
del num[0]
print(num)
num.pop()           #removes last value
print(num)
num[2] = 8
print(num)
num.clear()         #clears whole list(empty [])
print(num)

#Tuples - Immutable
tpl = (1, )          #Wont print as a tuple if comma is not put
print(tpl)
tpl1 = (1, 2, 3, 4)
idx = tpl1.index(3)
print(idx)

#Swapping
a = 6
b = 8
print(a, b)
a, b = b, a
print(a, b)

