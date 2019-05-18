import math
x1 = int(input("Enter x1 value:  "))
x2 = int(input("Enter x2 value:  "))
y1 = int(input("Enter y1 value:  "))
y2 = int(input("Enter y2 value:  "))
x2_x12= ((x2-x1) **2)
y2_y12 = (y2-y1)**2
cal= (x2_x12+y2_y12)
root = math.sqrt(cal)
print (root)
