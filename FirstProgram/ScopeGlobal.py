'''l = 10      #Global
def fun1(n):
    #l = 5       #Local
    m = 10      #Local
    global l        #Now this function is allowed to change the value of global l
    print(l, m)
    print("Hi", n)

fun1("Nidhi")
#print(m)   local
print(l)'''

def fun2():
    x = 10
    def fun3():
        global x        #creates a global variable
        x = 20        # and sets its value to 20
    print("Before calling fun3()", x)
    fun3()
    print("After calling fun3()", x)

fun2()
print(x)