# code30.py
# Day 2 Python Practice
# Write a program to find the power of a number (without using pow()).

base = int(input("ENTER THE BASE NUMBER:=\n"))
exponent = int(input("ENTER THE EXPONONT:=\n"))

result = pow(base , exponent)

print(f"{base} RAISED TO THE POWER {exponent} IS {result}")