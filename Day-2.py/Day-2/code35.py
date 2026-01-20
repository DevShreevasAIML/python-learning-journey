# Aim: To check whether a string is a palindrome
text = "madam"
if text == text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")