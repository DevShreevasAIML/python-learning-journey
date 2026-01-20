# code25.py
# Day 2 Python Practice
# Write a program to count the number of digits in a number.

num = int(input("Enter the number: \n"))

count = 0
temp = abs(num)

if temp == 0:
    count = 1
else :
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number of digits: \n{count}")