# Aim: To find LCM of two numbers
import math
a = 12
b = 15
lcm = abs(a * b) // math.gcd(a, b)
print(f"LCM of {a} and {b}: {lcm}")