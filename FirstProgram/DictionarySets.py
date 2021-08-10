#Dictionary- key value player
#keys can be numbers or strings
#values can be numbers, strings, lists, tuples, other dictionaries
d1 = {}
print(type(d1))
d2 = {"name":"Nidhi", "class":"CSIT", "subjects":{"1":"M3", "2":"ADA", "3":"DBMS"}}
print(d2)
print(d2["name"])
print(d2["subjects"])
print(d2["subjects"]["2"])
d2["dept"] = "CSIT Dept"
print(d2)
del d2["dept"]
print(d2)

#d3 = d2         #d3 is a pointer that points to d2, thus any change in d3 will make change in d2
d3 = d2.copy()      #copies d2 in d3

d2.update({"dept":"CSIT"})
print(d2)

print(d2.keys())
print(d2.items())

#Sets- only retains unique values
s = set()
print(type(s))
s.add(1)
s.add(1)
s.add(2)
print(s)
s1 = s.union({1, 2, 3})     #functions like union, intersection etc are applicable
print(s, s1)
print(s.isdisjoint(s1))
s.remove(2)
print(s)


#l = [1, 2, 3, 4]
#s_using_list = set(l)   OR
s_using_list = set([1, 2, 3, 4])
print(type(s_using_list))

