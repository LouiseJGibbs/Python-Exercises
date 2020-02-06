from array import *
import random

#094 Display position in array
nums = array('i', [])
for i in range(0,5):
    nums.append(random.randint(0,100))

print(nums)
d = int(input("What number would you like to find in the array? "))
while d not in nums:
    d = int(input("Number not in array, What number would you like to find in the array? "))

print(str(d) + " appears in position " + str(nums.index(d)) + " of the array")
