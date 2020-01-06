from array import *

#091 Repeated numbers
nums = array('i', [])
for i in range(0,5):
    n = int(input("Please enter a number: "))
    nums.append(n)
print(sorted(nums))

repeat = int(input("Please enter a number from the array: "))
print("This number appears in the array " + str(nums.count(repeat)) + " times")

