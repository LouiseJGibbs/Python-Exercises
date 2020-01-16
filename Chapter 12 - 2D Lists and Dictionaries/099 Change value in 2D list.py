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


