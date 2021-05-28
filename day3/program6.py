# take a number and find a factorial of that number.
num = int(input("Enter a number"))
fact = 1
if(num < 0):
    print("Factorial of negative number is not possible")
elif(num == 0):
    print("Factorial of 0 is 1")
for i in range(1, num+1):
    fact = fact*i
print("Factorial of", num, "is", fact)
