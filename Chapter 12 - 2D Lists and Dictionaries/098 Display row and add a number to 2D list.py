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
