# This is code53.py
# Reverse a given number.

i = int(input("Enter the number to reverse :-"))

rev = 0
i = abs(i)

while i > 0:
    digit = i % 10
    rev = rev * 10 + digit
    i //= 10

print(f"REVERSED NUMBER IS :- {rev}")