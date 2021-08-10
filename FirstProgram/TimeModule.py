import time

initial = time.time()       #Gives number of ticks(seconds)
for i in range(10):
    print("Hello World")
print(time.time() - initial)

initial1 = time.time()
i = 0
while i < 10:
    print("Hello World")
    time.sleep(2)           #time delay of two seconds while running of program code
    i += 1
print(time.time() - initial1)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
#time.time()        returns number of seconds(ticks)
#time.localtime()   converts ticks into local time in form of tuple
#time.asctime()     converts tuple into presentable time format
