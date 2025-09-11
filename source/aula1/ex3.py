t = float(input("Enter time (seconds): "))
a = 1.8*t + 0.6
v = 0.9*t**2 + 0.6*t
s = 0.3*t**3 + 0.3*t**2

print("Acceleration is:", round(a, 3))
print("Velocity is:", round(v, 3))
print("Position is:", round(s, 3))
