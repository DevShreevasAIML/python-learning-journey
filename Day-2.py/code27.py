# code27.py
# Day 2 Python Practice
# Write a program to print the Fibonacci series up to N terms.

while True:
    n = int(input("Enter number of terms: "))
    if n > 0:
        break
    else:
        print("Please enter a positive number")

a = 0
b = 1

if n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
