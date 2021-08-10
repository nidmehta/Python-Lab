#Creating files, folders and editing them
import os
#print(dir(os))
print(os.getcwd())          #get current working directory
#os.chdir("C://")
#print(os.getcwd())
#f = open("Nidhi.txt")

print(os.listdir())
print(os.listdir("C://"))

#os.mkdir("Misc")
#os.makedirs("Misc/Misc1")              #If Misc is there then creates Misc1 inside it or else first creates Misc then Misc1 inside it

#os.rename("Nidhi.txt", "Niddi.txt")

print(os.environ.get('Path'))

print(os.path.join())