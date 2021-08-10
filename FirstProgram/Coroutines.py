def searcher():
    import time
    #Some task which takes 5 seconds (delay)
    book = "Hello World, This is Nidhi"
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
             print("Yes, Text is in the book")
        else:
            print("No, Text is not in the book")

s = searcher()      #Creating object of coroutine searcher
print("Search Started")
next(s)             #Runs the code in coroutine
print("Next Method Run")
#After this coroutine starts, now only while loop is run one after another till all statements are executed
s.send("Nidhi")
input("Press Any Key")
s.send("Dosa")
s.close()       #Coroutine is closed and all resources are freed
#s.send("AAAAAAAa")