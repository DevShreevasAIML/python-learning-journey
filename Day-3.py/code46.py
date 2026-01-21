# This is code46.py
# Calculate the sum of numbers from 1 to N.

n = int(input("ENTER THE NUMBER : -"))

total = 0
for i in range(1 , n+1):
    total += i

print(f"SUM FROM 1 TO {n} IS : - {total}")