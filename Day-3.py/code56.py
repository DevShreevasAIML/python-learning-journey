# This is code56.py
# Print numbers between 1 and 100 that are divisible by 3.

n = int(input("Enter the number :- \n"))

print(f"Number between 1 and 100 div by {n}")

for i in range(1 , 101):
    if(i % n == 0):
        print(i , end =" ")