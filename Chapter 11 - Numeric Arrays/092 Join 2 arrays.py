from array import *
import random

#092 Join 2 arrays
nums = array('i', [])
m = 3
for i in range(0,m):
    n = int(input(str(m - i) + " numbers required. Please enter a number between 0 and 100: "))
    while n > 100 or n < 0:
            n = int(input("Invalid number. " + str(m - i) + " numbers required. Please enter a number between 0 and 100: "))
    nums.append(n)

numsR = array('i', [])
for i in range(0,m):
    numsR.append(random.randint(0,100))

for i in sorted(nums + numsR):
    print(i)
