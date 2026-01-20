# code29.py
# Day 2 Python Practice
# Write a program to check whether a year is a leap year.

year = int(input("Enter the Year: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("this is leap year" , year)

else:
    print("Not a leap year" , year)


    