# This is code64.py
# Find duplicate elements in a list.

lst = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = set([x for x in lst if lst.count(x) > 1])
print("Duplicate elements:", duplicates)
