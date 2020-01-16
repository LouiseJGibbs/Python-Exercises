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

