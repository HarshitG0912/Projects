a=int(input("enter a no.:"))
if(a%3==0 and a%2==0):
    print("num is div by both 2 and 3")
elif(a%2==0):
    print("num is div 2")
elif(a%3==0):
    print("num is div by 3.")
else:
    print("num is not div 2 or 3.")