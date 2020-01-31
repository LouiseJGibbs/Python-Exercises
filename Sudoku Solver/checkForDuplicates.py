import collections

totalSquares = 2
grid = [[1, 2, 4, 3],[1, 2, 1, 2],[2, 3, 4, 1],[4, 1, 2, 3]]
#grid = [[1, 2, 1, 1], [3, 2, 1, 1],[4, 2, 3, 1],[2, 2, 1, 1]] 
#grid = [[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7], [1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7],[1, 5, 6, 2, 7,1, 6,3,7]]

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


def main():

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

main()

