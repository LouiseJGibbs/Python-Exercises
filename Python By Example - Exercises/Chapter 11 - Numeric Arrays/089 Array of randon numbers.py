from array import *
import random

#089 Array of random numbers
nums= array('i', [])
for i in range(0,5):
    nums.append(random.randint(0, 100))

for i in sorted(nums):
    print(i)
