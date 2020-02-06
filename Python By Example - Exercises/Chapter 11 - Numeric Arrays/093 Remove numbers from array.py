from array import *

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
        

