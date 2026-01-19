# Check whether a number is a palindrome
# Aim: To check if a number reads the same forwards and backwards.

num = int(input("Enter a number: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")