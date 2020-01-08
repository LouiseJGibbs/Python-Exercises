from array import *

#088 5 integers in reverse order
nums = array('i', [])
for i in range(0,5):
    n = int(input("Please enter a number: "))
    nums.append(n)

print(nums)
nums= sorted(nums)
nums.reverse()

print(nums)
