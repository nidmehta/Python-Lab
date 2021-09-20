#Tuples - Immutable

#Tuple with one item
tpl = (1, )          #Wont print as a tuple if comma is not put
print(tpl)
print(type(tpl))

tpl1 = (1, 2, 3, 4)
print(len(tpl1))
idx = tpl1.index(3)
print(idx)

#Constructor tuple()
tpl2 = tuple(("aaa", "bbb", "ccc"))
print(tpl2)

#Swapping
a = 6
b = 8
print(a, b)
a, b = b, a
print(a, b)
