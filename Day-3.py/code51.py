# This is code51.py
# Count the number of digits in a given number.

n = int(input("Enter the number : - \n"))

count = 0
if( n == 0):
    count = 1
else:
    n = abs(n)
    while n > 0:
        n //=10
        count+=1

print("THIS IS NUMBER ", count)

