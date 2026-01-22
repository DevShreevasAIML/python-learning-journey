# This is code54.py
# Check whether a number is a palindrome or not.

i  = input("ENTER THE VALUE : =")

rev = i[::-1]

if(i == rev):
    print("Palindrome")
else:
    print("NOT")