# Take two numbers and display the gratest number.
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if(num1 > num2):
    print(num1, "is greater than", num2)
elif(num1 == num2):
    print("both the numbers are equal")
else:
    print(num2, "is greater than", num1)
