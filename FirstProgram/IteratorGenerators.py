#For traversing through an object
#Iterable- Tells if it can be iterated __iter__() or __get__()
#Iterator- __next__()
#Iteration-
#Generators- Iterators which can only be iterated once. Values are generated on the way/fly(That is generate then iterate the generate then iterate and so on)
#Generators can only be iterated once
def gen(n):     #Saves memory as values are generated on run and not stored in memory
    for i in range(n):
        yield i         #Not generated but can generate

g = gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
#print(g.__next__())

for i in range(10):        #Range is a generator
    print(i)

s = "NIDHI"         #Strings are Iterable
for i in s:
    print(i)

i = iter(s)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
#print(i.__next__())

#n = 12345
#no = iter(n)           #int object is not iterable


