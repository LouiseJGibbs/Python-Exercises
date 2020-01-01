import math

#032 volume of a cylinder
radius = int(input("Please enter the radius of a circle at the end of the cylinder: "))
circleArea = math.pi*(radius**2)
print("The area of the circle is", circleArea);

depth = int(input("Please enter the depth of the cylinder: "))
print("The volume of the cylinder is", round(circleArea*depth, 2))
