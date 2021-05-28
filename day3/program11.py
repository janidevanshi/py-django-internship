# Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .
num = int(input("Enter a number: "))
if(num >= 0):
    if(num == 0):
        print(num, " is zero")
    else:
        print(num, " is positive number")
else:
    print(num, " is negative number")
