#2D list to hold (x, y) 
points = [[0,0],[0,0]]

# User input for first point (x1,y1)
points[0][0] = int(input("Enter x1: "))
points[0][1] = int(input("Enter y1: "))

# User input for second point (x2,y2)
points[1][0] = int(input("Enter x2: "))
points[1][1] = int(input("Enter y2: "))

#Unpack lists into variables 
x1, y1 = points[0]
x2, y2 = points[1]

# Distance formula
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Result
print(f"distance between {points[0]} and {points[1]} is : {distance:.2f}")