num1 = input("Enter num 1: ")
num2 = input("Enter num 2: ")
try:
    print("Sum: ", int(num1)+int(num2))
except Exception as e:
    print(e)
finally:
    print("Hello")