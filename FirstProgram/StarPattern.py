n = int(input("Enter a number:"))
b = input("Enter 0 or 1:")
if b == "1":
    for i in range(1, n+1, 1):
        print(i * '*')
elif b == "0":
    for i in range(n, 0, -1):
        print(i * '*')