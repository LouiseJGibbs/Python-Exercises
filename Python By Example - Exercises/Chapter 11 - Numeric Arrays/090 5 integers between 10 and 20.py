from array import *

#090 5 integers between 10 and 20
nums = array('i', [])
m = 5
for i in range(0,m):
    n = int(input(str(m - i) + " numbers required. Please enter a number between 10 and 20: "))
    while n > 20 or n < 10:
            n = int(input("Invalid number. " + str(m - i) + " numbers required. Please enter a number between 10 and 20: "))
    nums.append(n)

print("Thankyou, here is the full array: ")
for i in sorted(nums):
    print(i)
            
