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

def getSquareWithGridRef(num, grid):
    square = []
    for i in range(1, totalColsInSquare + 1):
        if num < totalColsInSquare*i:
            start = (num - totalColsInSquare*(i-1)) * totalColsInSquare
            startCol = totalColsInSquare*(i-1)
            for j in range(startCol, totalColsInSquare*i):
                for k in range(start, start + totalColsInSquare):
                    square.append([grid[j][k], j, k])
            break
    return square

def getSquare(num, grid):
    square = []
    grid = getSquareWithGridRef(num, grid)
    for i in range(0, totalColsInSquare**2):
        square.append(grid[i][0])
    return square

def fillBlank_SingleNumberCheck(grid):
    change = False
    for i in range(0,totalColsInSquare**2):
        for j in range(0,totalColsInSquare**2):
            if grid[i][j] == 0:
                missingInRow = checkMissingNumbers(getrow(i,grid))
                if len(missingInRow) == 1:
                    grid[i][j] = missingInRow[0]
                    print("(Row) Position", i, j, "has been filled with", missingInRow[0])
                    change = True
                    break
                
                missingInCol = checkMissingNumbers(getcol(j, grid))
                if len(missingInCol) == 1:
                    grid[i][j] = missingInCol[0]
                    print("(Col) Position", i, j, "has been filled with", missingInCol[0])
                    change = True

                #elif len(missingInSquare):
                #    grid[i][j] = missingInSquare[0]
                #    print("(Square) Position", i, j, "has been filled with", missingInSquare[0])
                #    change = True
                #    break;

    for i in range(0, totalColsInSquare**2):
        missingInSquare = checkMissingNumbers(getSquare(i, grid))
        if len(missingInSquare) == 1:
            for j in getSquareWithGridRef(i, grid):
                if j[0] == 0:
                    row = j[1]
                    col = j[2]
                    
                    grid[row][col] = missingInSquare[0]
                    print("(Square) Position", row, col, "has been filled with", missingInSquare[0]) 
                    change = True
                    break
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
    grid = generateGridWithBlank(3)
    draw(grid)
    correct = checkCorrect(grid)
    change = True
    x = 0

    while change and not correct:
        input("Press any key to continue")
        print("Iteration", x)
        x = x + 1
        change = fillBlank_SingleNumberCheck(grid)
        correct = checkCorrect(grid)
        if change:
            draw(grid)

    if correct:
        print("Congratulations, we've completed the Sudoku grid")
    else:
        print("Sorry, we were unable to complete the Sudoku grid")

main()

