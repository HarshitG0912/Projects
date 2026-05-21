a=int(input("enter a year:"))
if(a%400==0):
    print("it's a leap year")
elif(a%4==0 and a%100!=0):
    print("it's a leap year")
else:
    print("it's not a leap year")