# code22.py
# Day 2 Python Practice
# 22. Print all odd numbers from 1 to N
# Aim: To print all odd numbers between 1 and N.

n = int(input("Enter the N :\n"))
print("===========its all odds number ===========")
for i in range(1 , n + 1):
    if(i % 2 == 1):
        print(f"its a odd number \n{i}")