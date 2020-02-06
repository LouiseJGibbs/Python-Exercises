from array import *
import random

#088 5 integers in reverse order
nums = array('i', [])
for i in range(0,5):
    n = int(input("Please enter a number: "))
    nums.append(n)

print(nums)
nums= sorted(nums)
nums.reverse()

print(nums)


#089 Array of random numbers
nums= array('i', [])
for i in range(0,5):
    nums.append(random.randint(0, 100))

for i in sorted(nums):
    print(i)

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
            
#091 Repeated numbers
nums = array('i', [])
for i in range(0,5):
    n = int(input("Please enter a number: "))
    nums.append(n)
print(sorted(nums))

repeat = int(input("Please enter a number from the array: "))
print("This number appears in the array " + str(nums.count(repeat)) + " times")

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

#093 Remove numbers from array
nums = array('i', [])
nums_deleted = array('i', [])
for i in range(0,5):
    n = int(input("Please enter a number: "))
    nums.append(n)
print(sorted(nums))

n = input("Would you like to add or remove a number from the arrange? [add/remove]: ").lower()
while n == "add" or n == "remove":
    if n=="add":
        nums.append(int(input("Please enter a number: ")))
    elif n == "remove":
        remove = int(input("Please enter a number from the array: "))
        if(remove in nums):
            nums.remove(remove)
            nums_deleted.append(remove)
            print("Number removed")
        else:
            print("Number not found")
    print(sorted(nums))
    n = input("Would you like to add or remove a number from the arrange? [add/remove]: ").lower()

print("No more changes can be made to the array")
print("Deleted numbers: " + str(sorted(nums_deleted)))
print("Complete array: " + str(sorted(nums)))

#094 Display position in array
nums = array('i', [])
for i in range(0,5):
    nums.append(random.randint(0,100))

print(nums)
d = int(input("What number would you like to find in the array? "))
while d not in nums:
    d = int(input("Number not in array, What number would you like to find in the array? "))

print(str(d) + " appears in position " + str(nums.index(d)) + " of the array")

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
        

