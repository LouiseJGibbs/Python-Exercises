#096 Simple 2D List

simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in range(0,len(simple_list)):
    print(simple_list[i][:])

#097 Select row and column from 2D List

simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
rowCount = len(simple_list) - 1

row = int(input("Please enter a row number between 0 and " + str(rowCount) + ": "))
while row > rowCount:
    row = int(input("Invalid number. Please enter a valid row number between 0 and " + str(rowCount) + ": "))

colCount = len(simple_list[row]) - 1
col = int(input("Please enter a column number between 0 and " + str(colCount) + ": "))
while col > colCount:
    col = int(input("Invalid number. Please enter a valid column number between 0 and " + str(colCount) + ": "))

print("row " + str(row) + ", col " + str(col) + ": " + str(simple_list[row][col]))

#098 Display row and add a number to 2D list

simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
rowCount = len(simple_list) - 1

row = int(input("Please enter a row number between 0 and " + str(rowCount) + ": "))
while row > rowCount:
    row = int(input("Invalid number. Please enter a valid row number between 0 and " + str(rowCount) + ": "))

print(simple_list[row])
simple_list[row].append(int(input("Please enter a number to add to the end of the row: ")))
print(simple_list[row])
print()

for i in range(0,len(simple_list)):
    print(simple_list[i][:])

#099 Change value in 2D list

simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
rowCount = len(simple_list) - 1

for i in range(0,len(simple_list)):
        print(simple_list[i][:])

change = 'y'
while change == 'y':
    
    row = int(input("Please enter a row number between 0 and " + str(rowCount) + ": "))
    while row > rowCount:
        row = int(input("Invalid number. Please enter a valid row number between 0 and " + str(rowCount) + ": "))
    
    print(simple_list[row])
    change = input("Would you like to change a number in this row? Y/N: ").lower()
    
    if change == "y":
        colCount = len(simple_list[row]) - 1
        col = int(input("Please enter a column number between 0 and " + str(colCount)+ ": "))
        
        while col > colCount:
            col = int(input("Invalid answer. Please enter a column number between 0 and " + str(colCount)+ ": "))
        
        simple_list[row][col] = int(input("Please enter the number you'd like to replace 'row " + str(row) + ", col " + str(col) + "' with: "))

    print("New Array: ")
    
    for i in range(0,len(simple_list)):
        print(simple_list[i][:])

    change = input("Would you like to change a number in this array? Y/N").lower()

#100 Create a dictionary

d = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
"Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
"Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

for i in d.keys():
    print(i, d[i])
  
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

#102 Name, Age, Shoe Size
d = {}

for i in range(1, 5):
    name = input("What is the name of person " + str(i) + "? ")
    age = int(input("How old is person " + str(i) + "? "))
    shoeSize= int(input("What is the shoe size of person " + str(i) + "? "))

    d[name] = {"age":age, "shoe size": shoeSize}

print(d)

name = input("Who would you like to see the details of? ")
if name in d:
    print(d[name])
else:
    print("Person not found")

#103 Name, Age, but not print Shoe Size
d = {}

for i in range(1, 5):
    name = input("What is the name of person " + str(i) + "? ").strip()
    age = int(input("How old is person " + str(i) + "? "))
    shoeSize= int(input("What is the shoe size of person " + str(i) + "? "))

    d[name] = {"age":age, "shoe size": shoeSize}

print(d)

name = input("Who would you like to see the details of? ")
if name in d:
    print("This persons age is " + str(d[name]["age"]))
else:
    print("Person not found")

#104 Remove someone
d = {}

for i in range(1, 5):
    name = input("What is the name of person " + str(i) + "? ").strip()
    age = int(input("How old is person " + str(i) + "? "))
    shoeSize= int(input("What is the shoe size of person " + str(i) + "? "))

    d[name] = {"age":age, "shoe size": shoeSize}

print(d)

name = input("Who would you like to remove? ")
if name in d:
    if input("Remove this record (Y/N): " + name + ": " +str(d[name])).lower() == "y":
        del d[name]
else:
    print("Person not found")

print("New Dictionary: ")
for name in d:
    print(name +  ": " + str(d[name]))




