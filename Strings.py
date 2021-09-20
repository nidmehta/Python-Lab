#String data type

#String Slicing
mystr = "Hello World Please Die"
print(len(mystr))       #prints the length of string
print(mystr[0:])        #prints whole string
print(mystr[:5])        #automatically takes 0
print(mystr[0:5])       #var[x:y] x included y excluded
print(mystr[0:45])      #prints whole string without giving error but gives erroe if print(mystr[45])
print(mystr[::])        #0:end:1
print(mystr[0:5:2])     #prints with 2 characters gap (the character printed is included in the two chracters)
print(mystr[-1::-1])       #prints from back of string to first

#String Functions
print(mystr.isalnum())      #False because it has spaces
print(mystr.endswith("ie"))
print(mystr.count("o"))
print(mystr.capitalize())       #Capitalizes the first letter of string only
print(mystr.find("Di"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("Die", "Live"))