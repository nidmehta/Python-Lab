#*args and **kwargs are optional arguments, i.e., if you don't give them in function cal there won't be any error
def nprint(a, b, c, d):
    print(a, b, c, d)
nprint("A", "B", "C", "D")

def function_args(arg, *args, **kwargs):       #Takes arguments in forms of tuples
    print(type(args))           #Tuple
    print(arg)
    for i in args:
        print(i)
    for key, value in kwargs.items():       #items() in an inbuilt function
        print(key, value)
arg = "Normal Argument"
l = ["A", "B", "C", "D", "E"]   #Doesn't matter what the datatype(list, tuple, etc) is here, *args always takes it as a tuple
dict = {"1":"A", "2":"B", "3":"C"}
function_args(arg, *l, **dict)

#def function_args(*args, arg):      #ERROR: Normal arguments should be before *args
#Convention: def function_name(arg, *args, **kwargs):

