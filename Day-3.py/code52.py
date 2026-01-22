# This is code52.py
# Find the sum of digits of a given number.

n = int(input("ENTER THE NUMBER := \n"))

sum = 0
n = abs(n)

while n > 0:
    digit = n % 10
    sum += digit
    n //= 10

print(f"this is the digits of sum:= {sum}")