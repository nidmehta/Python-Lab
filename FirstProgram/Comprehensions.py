#Reduces line of code

#List Comprehensions
l = []
for i in range(5):
    if i % 2 == 0:
        l.append(i)
print(l)
#OR
l = [i for i in range(5) if i % 2 == 0]
print(l)

#Dictionary Comprehensions
d = {i : f"Number {i}" for i in range(5) if i % 2 == 0}
print(d)
#To exchange keys with values in a dictionary
d = {val : key for key, val in d.items()}
print(d)

#Set Comprehensions
s = {i for i in [1, 2, 3, 3, 3, 4]}
print(s)
print(type(s))

#Generator Comprehensions
g = (i for i in range(5) if i % 2 == 0)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
#OR
for i in g:
    print(i)

