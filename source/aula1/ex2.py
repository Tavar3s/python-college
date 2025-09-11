import math as mt


p1 = list()
p2 = list()
p1.append(float(input("Enter p1.x: ")))
p1.append(float(input("Enter p1.y: ")))
p2.append(float(input("Enter p2.x: ")))
p2.append(float(input("Enter p2.y: ")))

d = mt.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print("Distance is:", d)
