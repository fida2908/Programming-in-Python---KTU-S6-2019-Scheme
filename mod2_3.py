 # Write a Python program to find distance between two points (xl,yl) and (x2,y2)

x1 = int(input("Enter x coordinate of point 1: "))
y1 = int(input("Enter y coordinate of point 1: "))
x2 = int(input("Enter x coordinate of point 2: "))
y2 = int(input("Enter y coordinate of point 2: "))

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
print(f"Distance: {distance}")