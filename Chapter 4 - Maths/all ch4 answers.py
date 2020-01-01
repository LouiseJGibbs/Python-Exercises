import math

#027 Multiply decimal
num = float(input("Enter number with lots of decimal places: "))
print(num, "x 2 =", num*2)

#028 Multiply decimal, 2 decimal places
num = float(input("Enter number with lots of decimal places: "))
print(round(num, 2), "x 2 =", round(num*2, 2))

#029 square root of number above 500
num = 0
while num < 500:
    num = int(input("Enter number that is greater than 500: "))

print("The square root of", num, "is", round(math.sqrt(num), 2))

#030 pi to 5 decimal places
print("PI = ", round(math.pi, 5))

#031 area of a circle
radius = int(input("Please enter the radius of a circle: "))
print("The area of the circle is", math.pi*(radius**2));

#032 volume of a cylinder
radius = int(input("Please enter the radius of a circle at the end of the cylinder: "))
circleArea = math.pi*(radius**2)
print("The area of the circle is", circleArea);

depth = int(input("Please enter the depth of the cylinder: "))
print("The volume of the cylinder is", round(circleArea*depth, 2))

#033 calculate remainder
num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))

divide = num1//num2
remainder = num1%num2

print(num1, "/", num2, "=", divide, "with", remainder, "left over")

#034 Area of triangle and square
print("1. Square")
print("2. Triangle")

num=0
while num!=1 and num!=2:
    num = int(input("Please enter a number: "))

if(num==1):
    height = int(input("Please enter the height of the square: "))
    print("The area of the square is", height**2)
else:
    height = int(input("Please enter the height of the triangle: "))
    base = int(input("Please enter the base of the triangle: "))
    print("The area of the triangle is", (height*base)/2)
