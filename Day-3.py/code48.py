# This is code48.py
# Print only even numbers from 1 to N.

n = int(input("ENTER THE NUMBER : - \n"))

for i in range(1 , n+1):
    if(i % 2 == 0):
        print(f"THIS IS EVEN NUMBER {i}")