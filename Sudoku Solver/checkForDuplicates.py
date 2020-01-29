import collections

def getsquare(col1, col2, row1, row2, grid):
    return [grid[col1][row1], grid[col1][row2], grid[col2][row1], grid[col2][row2]]

def getcol(col, grid):
    fullCol = []
    for i in range(0,4):
        fullCol.append(grid[i][col])
    return fullCol

def getrow(row, grid):
    return grid[row]

def checkDuplicates(data):
    seen = []
    duplicates = []
    for i in data:
        if i not in seen:
            seen.append(i)
        else:
            if i not in duplicates:
                duplicates.append(i)
    return duplicates

def redrawGrid(grid):
    print(grid[0][0:2], "|", grid[0][2:4])
    print(grid[1][0:2], "|", grid[1][2:4])
    print("---------------")
    print(grid[2][0:2], "|", grid[2][2:4])
    print(grid[3][0:2], "|", grid[3][2:4])

def main():
    totalSquares = 2
    grid = [[1, 2, 3, 4],[3, 4, 1, 2],[2, 3, 4, 1],[4, 1, 2, 3]]
    #grid = [[1, 2, 1, 1], [3, 2, 1, 1],[4, 2, 3, 1],[2, 2, 1, 1]] 

    redrawGrid(grid)

    #check horizonal
    for i in range(0, totalSquares**2):
        d = []
        d = checkDuplicates(getrow(i, grid))
        if not d:
            print("No errors when checking row", i)
        else:
            print("The following numbers were found more than once in row", i, ":", d)

    #check vertical
    for i in range(0, totalSquares**2):
        d = []
        d = checkDuplicates(getcol(i, grid))
        if not d:
            print("No errors when checking column", i)
        else:
            print("The following numbers were found more than once in col",i, ":", d)
            
    #checksquare
    d = []
    d.append(checkDuplicates(getsquare(0, 1, 0, 1, grid)))
    if not d:
        print("NO")
    else:
        print(d)
    d = []
    d.append(checkDuplicates(getsquare(0, 1, 2, 3, grid)))
    if not d:
        print("NO")
    else:
        print(d)
    d = []
    d.append(checkDuplicates(getsquare(2, 3, 0, 1, grid)))
    if not d:
        print("NO")
    else:
        print(d)
    d = []
    d.append(checkDuplicates(getsquare(2, 3, 2, 3, grid)))
    if not d:
        print("NO")
    else:
        print(d)
    d = []
    
    
main()

