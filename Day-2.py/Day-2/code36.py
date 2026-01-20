# Aim: To count vowels in a string
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Number of vowels: {count}")