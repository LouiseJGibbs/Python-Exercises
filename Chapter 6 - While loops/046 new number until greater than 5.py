#046 new number until greater than 5
num = int(input("Please enter a number less than 5: "))
while num < 5:
    num = int(input("Please enter a number less than 5: "))

print("The last number you entered was " + str(num))
