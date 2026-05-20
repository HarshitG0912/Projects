str= str(str("The USA has currency symbol of '$' and 1$=94.66 INR"))
length= len(str)#tells how many characters are there
occ= str.count("$")#tells how many times it occured
find= str.find("$") #tells the position when occured for the first time
print(length)
print(occ)
print(find)