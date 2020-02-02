import collections

totalSquares = 3
#grid = [[1, 2, 3, 4],[3, 4, 1, 2],[2, 3, 4, 1],[4, 1, 2, 3]]
grid = [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7],[3,4,5,6,7,8,9,1,2],[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8]]

def getcol(col, grid):
    fullCol = []
    for i in range(0,4):
        fullCol.append(grid[i][col])
    return fullCol

def getrow(row, grid):
    return grid[row]

def getSquare(num, grid):
    square = []
    for i in range(1, totalSquares + 1):
        if num < totalSquares*i:
            start = (num - totalSquares*(i-1)) * totalSquares
            startCol = totalSquares*(i-1)
            for j in range(startCol, totalSquares*i):
                for k in range(start, start + totalSquares):
                    square.append(grid[j][k])
            break
    return square

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


def main():

    correct = True

    #check horizonal
    for i in range(0, totalSquares**2):
        d = []
        d = checkDuplicates(getrow(i, grid))
        if d:
            print("The following numbers were found more than once in row", i, ":", d)
            correct = False

    #check vertical
    for i in range(0, totalSquares**2):
        d = []
        d = checkDuplicates(getcol(i, grid))
        if d:
            print("The following numbers were found more than once in col",i, ":", d)
            correct = False

    #check squares
    for i in range(0, totalSquares**2):
        d = []
        d = checkDuplicates(getSquare(i, grid))
        if d:
            print("The following numbers were found more than once in square", i, ":", d)
            correct = False

    if not correct:
        print("This Sudoku grid is not correct")
    else:
        print("This Sudoku grid has no duplicates")

main()

