import collections
import math
import random

totalColsInSquare = 4

def generateGrid():
    increase = 0
    end = totalColsInSquare**2 + 1
    grid = []
    for j in range(0,totalColsInSquare):
        for i in range(0,totalColsInSquare):
            start = 1 + i*totalColsInSquare + increase
            grid.append(list(range(start,end)) + list(range(1,start)))
        increase = increase + 1
    return grid

def generateRandomGrid():
    grid = []
    for i in range(0,totalColsInSquare**2):
        for j in range(0,totalColsInSquare**2):
            grid.append(random.sample(range(1, totalColsInSquare**2 + 5), totalColsInSquare**2))
    return grid

def generateGridWithBlank(numberBlank):
    grid = generateGrid()
    for i in range(0, len(grid[0])):
        for x in range(0, numberBlank):
            r = random.randint(0, len(grid) - 1)
            grid[i][r] = 0
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
            if grid[x][i] == 0:
                s = s + "   "
            elif grid[x][i] < 10:
                s = s + "0" + str(grid[x][i]) + " "
            else:
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

def getSquareNumber(row, col):
    return (col/totalColsInSquare) + (row/totalColsInSquare)

def fillBlank_SingleNumberCheck(grid):
    change = False
    for i in range(0,totalColsInSquare**2):
        for j in range(0,totalColsInSquare**2):
            if grid[i][j] == 0:

                missingInRow = checkMissingNumbers(getrow(i,grid))
                missingInCol = checkMissingNumbers(getcol(j, grid))
                #missingInSquare = checkMissingNumbers(getSquare(int(getSquareNumber(i,j)), grid))
                
                if len(missingInCol) == 1:
                    grid[i][j] = missingInCol[0]
                    print("(Row) Position", i, j, "has been filled with", missingInCol[0])
                    change = True
                    break;
                elif len(missingInRow) == 1:
                    grid[i][j] = missingInRow[0]
                    print("(Col) Position", i, j, "has been filled with", missingInRow[0])
                    change = True
                    break;
                #elif len(missingInSquare):
                #    grid[i][j] = missingInSquare[0]
                #    print("(Square) Position", i, j, "has been filled with", missingInSquare[0])
                #    change = True
                #    break;
                
    return change
                    
def checkMissingNumbers(data):
    missing = []
    for i in range(1, len(data) + 1):
        if i not in data:
            missing.append(i)
    return missing

def checkCorrect(grid):
    correct = True
    for i in range(0, totalColsInSquare**2):
        rowMissing = checkMissingNumbers(getrow(i,grid))
        colMissing = checkMissingNumbers(getcol(i,grid))
        squareMissing = checkMissingNumbers(getSquare(i,grid))
        if rowMissing:
            #print("The following numbers are missing from row",i,":",rowMissing)
            correct = False
        if colMissing:
            #print("The following numbers are missing from col",i,":",colMissing)
            correct = False
        if squareMissing:
            #print("The following numbers are missing from square",i,":",squareMissing)
            correct = False
    if not correct:
        print("This Sudoku grid is not correct")
    else:
        print("This Sudoku grid is complete")
    return correct

def main():
    #grid = generateRandomGrid()
    grid = generateGridWithBlank(2)
    draw(grid)
    correct = checkCorrect(grid)
    change = True
    x = 0

    while change and not correct:
        print("Iteration", x)
        x = x + 1
        change = fillBlank_SingleNumberCheck(grid)
        correct = checkCorrect(grid)
        if change:
            draw(grid)
        if not change:
            for i in range(0, 3):
                print("Final Attempt", i)
                change = fillBlank_SingleNumberCheck(grid)
            
            

    print("Can't complete anymore")

main()

