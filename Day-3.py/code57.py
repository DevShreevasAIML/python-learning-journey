# This is code57.py
# Check whether a given number is prime or not.

n = int(input("Enter the value:- \n"))

if (n <= 1):
    print("Not prime")
else:
    for i in range (2 , n):
        if( n % i == 0):
            print("not prime number")
            break
    else:
        print("prime number")