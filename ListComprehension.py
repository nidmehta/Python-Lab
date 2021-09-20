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

#List Comprehension
lis = ["aaa", "baaa", "cbb", "dbbaaa", "ecc"]
newlis = [x for x in lis if "b" in x]
print(newlis)