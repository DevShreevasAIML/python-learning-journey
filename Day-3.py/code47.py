# This is code47.py
# Print the multiplication table of a given number.

n = int(input("ENTER THE TABLE NUMBER:- \n"))
print(f"=========TABLE OF {n}==============")
for i in range(1 , 11):
    print(f"{n} X {i} = {n * i}")