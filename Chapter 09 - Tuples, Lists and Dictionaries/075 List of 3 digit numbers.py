#075 List of 3 digit numbers
numbers = [123, 523, 623, 723]
n = int(input("Please type in a 3 digit number: "))

if n in numbers:
    print("Well done, this number appears in position " + str(numbers.index(n) + 1))
else:
    print("Number not found")

print(numbers)
