# code26.py
# Day 2 Python Practice
# Write a program to check whether a number is an Armstrong number.

n = int(input("Enter the number :- \n"))

digits = len(str(n))
temp = n
sum = 0

while temp > 0:
    digit = temp  % 10
    sum = sum + digit ** digits
    temp = temp // 10

if(sum == n):
    print("its arms")
else:
    print("Not")