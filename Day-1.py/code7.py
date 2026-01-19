# Divide two numbers
# Aim: To perform division and handle zero division error.

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
if b != 0:
    print("Quotient:", a / b)
else:
    print("Cannot divide by zero")