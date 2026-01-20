# code23.py
# Day 2 Python Practice
# 23. Find the sum of even numbers from 1 to N
# Aim: To find the sum of all even numbers between 1 and N
N = int(input("Enter N :- \n"))

sum_even = 0
for i in range (1, N + 1):
    if i % 2 ==0:
        sum_even += i

print(f"Sum of even number:- {sum_even}")