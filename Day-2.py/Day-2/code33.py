# Aim: To count positive and negative numbers in a list
numbers = [10, -5, 20, -15, 0, 25]
positive = sum(1 for i in numbers if i > 0)
negative = sum(1 for i in numbers if i < 0)
print(f"Positive numbers: {positive}, Negative numbers: {negative}")