#079 List of numbers
nums = []

for i in range(0,3):
    nums.append(int(input("Please enter a number to add to the list: ")))
    print(nums)

while input("Would you like to add another number to the list? Yes/No: ").lower() != "no":
    nums.append(int(input("Please enter a number to add to the list: ")))
    print(nums)
    if input("Are you sure you want to add this number to the list? Yes/No: ").lower() == "no":
        del nums[len(nums) - 1]
    print(nums)

for i in nums:
    print(i)
