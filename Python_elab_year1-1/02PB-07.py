x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
import math
a1 = x**y+z
a2 = math.cos(0)+math.log(x,math.e)
a3 = math.fabs(x)+math.fabs(y)
a4 = (x**2+y**2+z**2)**(1/2)
a5 = math.sin(x)**2 + math.cos(x)**2
a6 = math.pow(x+y,1/5)
a7 = (math.e**x)**math.log(y,math.e)
print("a1 = %.2f"%a1)
print("a2 = %.2f"%a2)
print("a3 = %.2f"%a3)
print("a4 = %.2f"%a4)
print("a5 = %.2f"%a5)
print("a6 = %.2f"%a6)
print("a7 = %.2f"%a7)