import math as mt


beta = float(input("Enter beta: "))
gamma = float(input("Enter gamma: "))
n = float(input("Enter n: "))

alpha = ((mt.e**beta)/gamma) * mt.sin(mt.radians(n))
print("Alpha is:",round(alpha, 3))
