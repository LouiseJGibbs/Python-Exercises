import collections

totalSquares = 3
#grid = [[1, 2, 4, 3],[1, 2, 1, 2],[2, 3, 4, 1],[4, 1, 2, 3]]
#grid = [[1, 2, 1, 1], [3, 2, 1, 1],[4, 2, 3, 1],[2, 2, 1, 1]] 
grid = [[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7], [1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7]]

def draw(grid):
    
    drawLine()
    for x in range(0, totalSquares**2):
        if x%totalSquares == 0 and x != 0:
            drawLine()
        s = " | "
        for i in range(0, totalSquares**2):
            if i%totalSquares == 0 and i != 0:
                s = s + "| "
            s = s + str(grid[x][i]) + " "
        print(s + "|")
    drawLine()

def drawLine():
    s = " -"
    for i in range(0, ((totalSquares**2) * 2) + (2*totalSquares) - 1):
            s = s + "-"
    print(s + "-")

def main():
    draw(grid)

main()
