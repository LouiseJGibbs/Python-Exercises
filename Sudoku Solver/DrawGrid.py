import collections
import math

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
        
def draw(grid):
    totalColsInSquare = int(math.sqrt(len(grid)))
    drawLine(totalColsInSquare)
    for x in range(0, totalColsInSquare**2):
        if x%totalColsInSquare == 0 and x != 0:
            drawLine(totalColsInSquare)
        s = " | "
        for i in range(0, totalColsInSquare**2):
            if i%totalColsInSquare == 0 and i != 0:
                s = s + "| "
            if grid[x][i] < 10:
                s = s + "0"
            s = s + str(grid[x][i]) + " "

        print(s + "|")
    drawLine(totalColsInSquare)

def drawLine(totalColsInSquare):
    s = " -"
    for i in range(0, ((totalColsInSquare**2) * 3) + (2*totalColsInSquare) - 1):
            s = s + "-"
    
    print(s + "-")

def main():
    grid = generateGrid(6)
    draw(grid)

main()
