#051 10 Green Bottles
for num in range(10, 0, -1):
    bottlesString = str(num) + " green bottles, hanging on the wall.\n" + str(num) + " green bottles, hanging on the wall.\nAnd if 1 green bottle should accidentally fall"
    print(bottlesString)
    while int(input("How many bottles will be hanging on the wall? ")) != num-1:
              print("Try again")
    print("There will be ", str(num - 1), "hanging on the wall")
