# This is code42.py
# Take a number as input and identify whether it is positive, negative, or zero.

n = int(input("Enter the number :- \n"))

if(n > 0):
    print(f"ITS A POSITIVE NUMBER:- {n}")
elif(n < 0):
    print(f"ITS A NEGATIVE NUMBER :- {n}")
else:
    print(f"ITS A ZERO NUMBER :- {n}")