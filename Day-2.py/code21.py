# code21.py
# Day 2 Python Practice
# 21. Print all even numbers from 1 to N
# Aim: To print all even numbers between 1 and N.

N = int(input("Enter the N :\n"))

for i in range(1 , N + 1):
    if( i % 2 == 0):
        print(f"its a even number \n{i}")