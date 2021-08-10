l = ["AAA", "BBB", "CCC", "DDD", "EEE"]
#else with for loop works only when for loop is completely iterated or does not have break statement
#for i in l:
#    print(i)
#    #break
#else:
#    print("For Loop Ended Properly")

#Use when the is some flag condition in the problem like searching for an element
for i in l:
    if i == "CC":
        break
else:
    print("Not Found")

