# solves a 9x9 sudoku board from column by column (going top down first, then left right)
# assumes the board is the correct size, and valid
# TODO: add a check before solving the board to verify it is valid (unique and solvable)


def main():
    grid = [[7,2,3,0,0,0,1,5,9],
            [6,0,0,3,0,2,0,0,8],
            [8,0,0,0,1,0,0,0,2],
            [0,7,0,6,5,4,0,2,0],
            [0,0,4,2,0,7,3,0,0],
            [0,5,0,9,3,1,0,4,0],
            [5,0,0,0,7,0,0,0,3],
            [4,0,0,1,0,3,0,0,6],
            [9,3,2,0,0,0,7,1,4]]

    if solve(grid):
        for row in grid:
            for num in row:
                print(num, end=" ")
        print("\n")
    else:
        print("Grid is unsolvable")



def solve(grid:"list"):
    coords = findEmptySquare(grid)  # get the coords of the next empty square
    if not coords: # there are no empty squares left, grid is solved
        return True

    for i in range(1, 10): # try placing every number 1-9 in that square
        if isSafe(i, coords, grid):
            grid[coords[1]][coords[0]] = i
            if solve(grid): # if a number is safe, recur, going to next square
                return True # if any number 1-9 does not work, backtrack
        grid[coords[1]][coords[0]] = 0
    return False

# iterate from left to right and top to bottom through the grid.
# return a tuple (x, y) representing the index of the first 0 in the grid, which is to say the first empty square
# if we reach the end of the grid without finding a 0, it must be all filled in, so return false
def findEmptySquare(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[j][i] == 0:
                return (i, j)
    return False


# check to see if placing num at the specified (x, y) coords in the grid is safe
# check for duplicate num in column, row, and box
# return true if safe, false otherwise
# num is the number to be inserted
# coords is the index of where in grid to insert num, stored as (x, y) or (column, row)
def isSafe(num, coords, grid):
    for entry in grid[coords[1]]: # if the number is a duplicate in its row
        if num == entry:
            return False

    for row in grid: # if the number is a duplicate in its column
        if row[coords[0]] == num:
            return False

    # if the number is a duplicate in its 3x3 box
    x = coords[0] // 3
    y = coords[1] // 3

    for i in range(x*3, (x*3) + 3):
        for j in range(y*3, (y*3) + 3):
            if num == grid[j][i]:
                return False

    return True

if __name__ == "__main__":
    main()