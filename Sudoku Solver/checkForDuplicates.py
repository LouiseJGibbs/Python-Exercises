import collections
import math


grid = [[1, 2, 3, 3],[3, 4, 1, 2],[2, 3, 4, 1],[4, 1, 2, 3]]
#grid = [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7],[3,4,5,6,7,8,9,1,2],[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8]]
totalCols = int(math.sqrt(len(grid)))

def getcol(col, grid):
    fullCol = []
    for i in range(0,totalCols):
        fullCol.append(grid[i][col])
    return fullCol

def getrow(row, grid):
    return grid[row]

def getSquare(num, grid):
    square = []
    for i in range(1, totalCols + 1):
        if num < totalCols*i:
            start = (num - totalCols*(i-1)) * totalCols
            startCol = totalCols*(i-1)
            for j in range(startCol, totalCols*i):
                for k in range(start, start + totalCols):
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

    for i in range(0, totalCols**2):
        rowDuplicates = checkDuplicates(getrow(i,grid))
        colDuplicates = checkDuplicates(getcol(i,grid))
        squareDuplicates = checkDuplicates(getSquare(i,grid))
        if rowDuplicates:
            print("The following numbers were found more than once in row",i, ":", rowDuplicates)
            correct = False
        if colDuplicates:
            print("The following numbers were found more than once in col",i, ":", colDuplicates)
            correct = False
        if squareDuplicates:
            print("The following numbers were found more than once in square", i, ":", squareDuplicates)
            correct = False

    if not correct:
        print("This Sudoku grid is not correct")
    else:
        print("This Sudoku grid has no duplicates")

main()

