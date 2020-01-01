import math

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
