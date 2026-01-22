# This is code62.py
# Count the number of even elements in a list.

n = [10 ,37 , 93, 82 ,98 ,2]
count = 0

for i in n:
    if i % 2 == 0:
        count += 1

print("Number of even element:= " , count)