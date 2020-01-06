from array import *
import random

#095 Divide array
nums = array('f', [])
for i in range(0,5):
    nums.append(random.randint(10, 100))
print(nums)

divide = int(input("Please enter a number between 2 and 5 "))
while divide < 2 or divide > 5:
    divide = int(input("Invalid answer. Please enter a number between 2 and 5 "))

for i in range(0,len(nums)):
    nums[i] = round(nums[i]/divide, 2)

print(nums)
