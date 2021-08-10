#Any string or character can be uses instead of 'and'
l = ["AAA", "BBB", "CCC", "DDD"]
for i in l:
    print(i, "and", end=" ")        #there will be an extra 'and' at the end of list
print("others")

a = " and ".join(l)                 #there wont be any extra 'and' at the end of list
print(a, "and others")