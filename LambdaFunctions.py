#Lambda Functions

(lambda x,y: x+y )(5,6)
def func1(x):
    return x+5
func1(5)

#filter (func, iterable )
list1= [1,2,3,4,5,6]
result=list(filter (lambda x:x%2==0,list1))
print(result)

#map (func, iterable)
print(list(map(lambda x:pow(x,3), list1)))

list2=[2,3,4,5,6]
print(list((map(lambda x:x*2, list2))))

list3=[9,8,7,6,5,6,7]
print(list(map (lambda x,y: x+y, list2, list3)))

l= [ '12345', 'cat', 'dog']
print(list(map(list,l)))

cube= lambda y: y**3
print(cube(5))

table= [lambda j=x: 2*j for x in range(1,11)]
for i in table:
  print(i())

list1=[1,2,3,4,5]
double= [lambda x=x: x*x for x in list1]
for i in double:
  print(i())

mylist = map(lambda x : x*2, [x for x in range(1,11)])
print(list(mylist))

list1=[1,2,3,4]
print(list(map(lambda x : x*2 , list1)))

from functools import reduce
li=[5,6,7,8,9,10,11]
sum = reduce (lambda x,y :x+y, li)
print(sum)

from functools import reduce
li=[5,6,7,8,9,10,11]
max = reduce (lambda x,y :x if x>y else y, li)
print(max)

age=[5,6,7,8,9,10,11]
print(list(filter(lambda x: x<10, age)))

str1= ['dog', 'cat']
print(list(map(lambda x: x.upper(), str1)))

#MAP FUNCTION
#l = ["1", "22", "333", "4444"]
#for i in range(len(l)):
#    l[i] = int(l[i])
#print(l[0] + 1)
#OR map iis used for type conversion as input is always a string in python
#l = list(map(int, l))       #map returns a memory location and then type casted to list
#print(l[0] + 1)


#l1 = [1, 2, 3, 4, 5]
#s = list(map(lambda x: x*x, l1))        #instead of writing a separate function lambda is used
#print(s)


#def sq(a):
#    return a*a
#def cube(a):
#    return a*a*a
#func = [sq, cube]
#for i in range(5):
#    val = list(map(lambda x:x(i), func))
#    print(val)




#FILTER
#l2 = [1, 2, 3, 4, 5, 6, 7, 8]
#def is_greater_4(n):
#    return n > 4
#nums = list(filter(is_greater_4, l2))       #filter filters true values from false values
#print(nums)




#REDUCE (improves time)
from functools import reduce
l3 = [1, 2, 3, 4]
#sum = 0
#for i in l3:
#    sum += i
#print(sum)
#OR
sum = reduce(lambda x, y: x + y, l3)
print(sum)
