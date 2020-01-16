#101 Change value in dictionary
d = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
"Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
"Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

for i in d.keys():
    print(i, d[i])

change = input("Would you like to make a change? Y/N: ").lower()
while change == "y":
    print("Available keys: " + str(d.keys()))
    name = input("Please enter the key you'd like to change: ")
    while name not in d.keys():
        print("Invalid answer, available keys: " + str(d.keys()))
        name = input("Please enter the key you'd like to change: ")

    print(d[name])

    change = input("Would you like to change a region? Y/N: ").lower()
    if change=="y":
        print("Available regions: " + str(d[name].keys()))
        region = input("Please enter the region you'd like to change: ")
        while region not in d[name].keys():
            print("Invalid answer, available regions: " + str(d[name].keys()))
            region = input("Please enter the region you'd like to change: ")

        d[name][region] = int(input("Please enter the new number"))

    print("List of regions for " + name)
    print(d[name])

    change = input("Would you like to make a change? Y/N: ").lower()

print("Final list of names and regions")
for i in d.keys():
    print(i, d[i])
