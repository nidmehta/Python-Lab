def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print(factorial(num))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))