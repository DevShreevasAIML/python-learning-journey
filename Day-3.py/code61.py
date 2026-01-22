# This is code61.py
# Find the largest element in a list.

n = [932, 327, 8732, 8632, 93]
largest = n[0]

for n in n:
    if n > largest:
        largest = n
print("Largest number:=" , largest)