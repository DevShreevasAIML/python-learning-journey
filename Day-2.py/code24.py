# code24.py
# Day 2 Python Practice
# Write a program to find the sum of odd numbers from 1 to N.

N = int(input("Enter N :- \n"))

sum_odd = 0
for i in range (1, N + 1):
    if i % 2 == 1:
        sum_odd += i

print(f"Sum of odd number:- {sum_odd}")