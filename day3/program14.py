# Write a program to swap 2 numbers without taking third variable.
a = int(input("Enter Number :"))
b = int(input("Enter Number :"))

a = a + b
b = a - b
a = a - b
print(a, "First number after swapping", b, "Second number after swapping")
