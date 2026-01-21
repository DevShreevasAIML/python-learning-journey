# This is code43.py
# Take two numbers and print the larger one.
number = []
for i in range(3):
    n = int(input(f"ENTER THE NUMBER {i+1}:- \n"))
    number.append(n)

largest = number[0]

for n in number:
    if n > largest:
        largest = n

print(f"Largest number is :- \n {i} is a largest number" , largest)