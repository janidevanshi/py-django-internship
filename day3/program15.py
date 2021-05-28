# Take starting number and ending number from the user and print following series.
# 30,27,24,21...0
num1 = int(input("Enter starting Number"))
num2 = int(input("Enter ending number"))
# for i in range(num1, num2, -1):
#     if(i % 3 == 0):
#         print(i)
# for i in range(num1, num2, -3):
#     print(i)
while (num1 >= num2):
    print(num1)
    num1 = num1 - 3
