
# Python program to find the average of five numbers
# total sum of five numbers
total_sum = 0
for n in range(5):
    # take inputs
    num = float(input('Enter number: '))
    # calculate total sum of numbers
    total_sum += num

# calculate average of numbers
avg = total_sum / 5

# print average value
print('Average of numbers =', avg)
