# code28.py
# Day 2 Python Practice
# Write a program to find the smallest of three numbers.

a = int(input("Enter the A value \n"))
b = int(input("Enter the B value \n"))
c = int(input("Enter the C value \n"))

if(a <= b and a <= c):
    print(f"THIS A VALUE AND THIS IS SMALLEST NUMBER:-\n{a}")
elif(b <= a and b <= c):
    print(f"THIS B VALUE AND THIS IS SMALLEST NUMBER:-\n {b}")
else:
    print(f"THIS C VALUE AND THIS IS SMALLEST NUMBER:-\n {c}")

# Ab ascending order
if a <= b and a <= c:
    first = a
    if b <= c:
        second = b
        third = c
    else:
        second = c
        third = b
elif b <= a and b <= c:
    first = b
    if a <= c:
        second = a
        third = c
    else:
        second = c
        third = a
else:
    first = c
    if a <= b:
        second = a
        third = b
    else:
        second = b
        third = a

print(f"Order: - \n {first} \n {second} \n {third}")