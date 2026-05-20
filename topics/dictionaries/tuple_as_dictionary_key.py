import math

#List of tuples
points = [(1, 2), (3, 4), (0, 5)]

#Empty dictionary to hold the output
result = {}

#Unpacking tuples in loop
for x, y in points:
    #Distance formula
    distance = round(math.sqrt(x**2 + y**2),2)
    result[x,y] = distance
print(result)