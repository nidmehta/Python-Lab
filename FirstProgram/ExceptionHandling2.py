f1 = open("Nidhi.txt")

try:
    f = open("xyz.txt")

except Exception as e:
    print(e)

except EOFError as e:
    print("EOFError: ", e)

except IOError as e:
    print("IOError: ", e)

else:
    print("This will run if except is not running")

finally:                #Used for code cleanup
    print("This will run anyway/ in any case")
    f1.close()

print("Done")
