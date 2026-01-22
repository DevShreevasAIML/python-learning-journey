# This is code58.py
# Print all prime numbers from 1 to N.

N = int(input("Enter N: "))

for num in range(2, N + 1):     # 2 se start (1 prime nahi hota)
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
