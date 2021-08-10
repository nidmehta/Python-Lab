def f1():
    print("Hi")
f2 = f1
#del f1             #if f1() is deleted then also f2 will print as f2 has a different memory location than f1
f2()


#A function can return a function
def f3(num):
    if num == 0:
        return print
    if num == 1:
        return sum
print(f3(0))


#A function can be given as an argument
def f4(f):
    f("this")
f4(print)


#Decorators- use when we have to do similar thing with many functions
def dec(f5):
    def status():
        print("Hi")
        f5()
        print("Bye")
    return status

#def nm():
#    print("Niddi")
#nm = dec(nm)           #or use @decorator_function_name
#nm()
#OR
@dec
def nm():
    print("Niddi")
nm()