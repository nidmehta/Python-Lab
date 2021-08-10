"""Modes
"r" - Open file for reading (default)
"w" - Open file for writing (deletes previous content every time the file is opened)
"x" - Creates file if not exists otherwise gives error
"a" - Add more content to existing file
"t" - Text mode (default)
"b" - Binary mode
"+" - Read and Write
"""
#f = open("filename","ab")    #a- what you want to do with file, b- type of file
#f = open("Nidhi.txt", "r")   #open() returns a pointer and f stores it
#content = f.read()
#print(content)         #Reads the full file
#content = f.read(3)         #Reads the first 3 characters
#print(content)
#content = f.read(3)         #Reads the next 3 characters
#print(content)
#for line in content:        Reads file character wise
#for line in f:              #Reads file line by line
#    print(line)             #Prints new line because the file has a new line character ater each line( can use end = "" to remove it)
#print(f.readline())            #Read a single line
#print(f.readline())             #Reads the next line
#print(f.readlines())            #To print file content as list
#f.close()               #To free the resources used while processing the file

#f = open("Nidhi1.txt", "w")
#f.write("My name is Niddi")
#f.close()

#f = open("Nidhi1.txt", "a")
#a= f.write("My name is Niddi")          #write() returns number of characters in the text file
#print(a)                #prints total characters in the text file
#f.close()

#Handle read and write both
#f = open("Nidhi1.txt", "r+")
#print(f.read())
#f.write("Thank you")
#f.close()

#Deleting a file
#f = open("Nidhi2.txt", "x")
#f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#import os
#if os.path.exists("Nidhi2.txt"):
#    os.remove("Nidhi2.txt")
#else:
#    print("File does not exist")
#To remove directory- os.rmdir("Dname")

#f = open("Nidhi1.txt")
#print(f.tell())         #tells the position of file pointer
#print(f.readline())
#print(f.tell())
#print(f.readline())
#print(f.tell())
#print(f.readline())
#f.seek(10)              #takes file pointer to the given position
#print(f.readline())
#f.close()

#With block doesn't require to close the file
with open("Nidhi1.txt") as f:
    a = f.readlines()
    print(a)

f = open("Nidhi1.txt")
print(f.readlines())
f.close()