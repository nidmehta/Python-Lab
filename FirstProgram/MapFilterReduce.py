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