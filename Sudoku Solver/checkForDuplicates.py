import collections
import math


grid = [[3, 2, 3, 4],[3, 4, 1, 2],[2, 3, 4, 1],[4, 1, 2, 3]]
#grid = [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7],[3,4,5,6,7,8,9,1,2],[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8]]
totalCols = int(math.sqrt(len(grid)))

def getcol(col, grid):
    fullCol = []
    for i in range(0,totalCols**2):
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

def checkMissingNumbers(data):
    missing = []
    for i in range(1, totalCols**2 + 1):
        if i not in data:
            missing.append(i)
    return missing

def main():
    correct = True

    for i in range(0, totalCols**2):
        rowMissing = checkMissingNumbers(getrow(i,grid))
        colMissing = checkMissingNumbers(getcol(i,grid))
        squareMissing = checkMissingNumbers(getSquare(i,grid))
        if rowMissing:
            print("The following numbers are missing from row",i,":",rowMissing)
            correct = False
        if colMissing:
            print("The following numbers are missing from col",i,":",colMissing)
            print(getcol(i,grid))
            correct = False
        if squareMissing:
            print("The following numbers are missing from square",i,":",squareMissing)
            correct = False

    if not correct:
        print("This Sudoku grid is not correct")
    else:
        print("This Sudoku grid has no duplicates")

main()

