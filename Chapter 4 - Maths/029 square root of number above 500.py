import math

#029 square root of number above 500
num = 0
while num < 500:
    num = int(input("Enter number that is greater than 500: "))

print("The square root of", num, "is", round(math.sqrt(num), 2))

