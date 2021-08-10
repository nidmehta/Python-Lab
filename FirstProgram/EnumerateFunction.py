l = ["A", "B", "C", "D", "E", "F"]
#instead of normal for loop with range(), we can use enumerate()
for i, item in enumerate(l):
    if i % 2 == 0:
        print(item)