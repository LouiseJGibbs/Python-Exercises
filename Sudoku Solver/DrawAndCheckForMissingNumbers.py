import collections
import math
import random

totalColsInSquare = 4

def generateGrid(sizeOfSquare):
    increase = 0
    end = sizeOfSquare**2 + 1
    grid = []
    for j in range(0,sizeOfSquare):
        for i in range(0,sizeOfSquare):
            start = 1 + i*sizeOfSquare + increase
            grid.append(list(range(start,end)) + list(range(1,start)))
        increase = increase + 1
    return grid

def generateRandomGrid(sizeOfSquare):
    grid = []
    for i in range(0,sizeOfSquare**2):
        for j in range(0,sizeOfSquare**2):
            grid.append(random.sample(range(1, sizeOfSquare**2 + 5), sizeOfSquare**2))
    return grid

def draw(grid):
    drawLine()
    for x in range(0, totalColsInSquare**2):
        if x%totalColsInSquare == 0 and x != 0:
            drawLine()
        s = " | "
        for i in range(0, totalColsInSquare**2):
            if i%totalColsInSquare == 0 and i != 0:
                s = s + "| "
            if grid[x][i] < 10:
                s = s + "0"
            s = s + str(grid[x][i]) + " "

        print(s + "|")
    drawLine()

def drawLine():
    s = " -"
    for i in range(0, ((totalColsInSquare**2) * 3) + (2*totalColsInSquare) - 1):
            s = s + "-"
    
    print(s + "-")

def getcol(col, grid):
    fullCol = []
    for i in range(0,totalColsInSquare**2):
        fullCol.append(grid[i][col])
    return fullCol

def getrow(row, grid):
    return grid[row]

def getSquare(num, grid):
    square = []
    for i in range(1, totalColsInSquare + 1):
        if num < totalColsInSquare*i:
            start = (num - totalColsInSquare*(i-1)) * totalColsInSquare
            startCol = totalColsInSquare*(i-1)
            for j in range(startCol, totalColsInSquare*i):
                for k in range(start, start + totalColsInSquare):
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
    for i in range(1, len(data) + 1):
        if i not in data:
            missing.append(i)
    return missing

def main():
    #grid = generateRandomGrid(totalColsInSquare)
    grid = generateGrid(totalColsInSquare)
    draw(grid)

    correct = True

    for i in range(0, totalColsInSquare**2):
        rowMissing = checkMissingNumbers(getrow(i,grid))
        colMissing = checkMissingNumbers(getcol(i,grid))
        squareMissing = checkMissingNumbers(getSquare(i,grid))
        if rowMissing:
            print("The following numbers are missing from row",i,":",rowMissing)
            correct = False
        if colMissing:
            print("The following numbers are missing from col",i,":",colMissing)
            correct = False
        if squareMissing:
            print("The following numbers are missing from square",i,":",squareMissing)
            correct = False

    if not correct:
        print("This Sudoku grid is not correct")
    else:
        print("This Sudoku grid is complete")

main()

