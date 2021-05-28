# Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

a = int(input("Enter Number"))
if(a < 100):
    print(a, "is less than 100")
    if(100 % 2 == 0):
        print(a, "is even")
    else:
        print(a, "is odd")
else:
    print(a, "is greater than 100")
