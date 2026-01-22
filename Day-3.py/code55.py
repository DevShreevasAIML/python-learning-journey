# This is code55.py
# Check whether a number is an Armstrong number or not.

i = int(input("Enter the number \n"))

temp = abs(i)

digits = len(str(temp))

sum_pow = 0
copy = temp

while copy > 0:
    digit = copy % 10
    sum_pow += digit ** digits
    copy //=10

if sum_pow == temp:
    print("ARMS strong")
else:
    print("not")
