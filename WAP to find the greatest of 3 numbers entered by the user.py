a=int(input("Enter your first no.:"))
b=int(input("Enter your second no.:"))
c=int(input("Enter your third no.:"))
if (a>=b and a>=c):
    print("among the given values the greatest is",a)
elif(b>=c and b>=a):
    print("among the given values the greatest is",b)
else:
    print("among the given values the greatest is",c)