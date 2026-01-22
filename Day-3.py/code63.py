# This is code63.py
# Reverse a list without using built-in functions.

n = [43, 323 ,834, 34 ,323]
rev =[]

for i in range(len(n)- 1, - 1, - 1):
    rev.append(n[i])

print("Rev list:-" ,rev)

#buiit in function

# n.reverse()
# print("rev" , n)