grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

## Teaches the uses of a nested for loop
def printGrid(grid):
    for x in range(9):
        if x > 0:
            # to not create an empty line when the program gets executed
            print()
        else:
            continue
        for y in range(6):
            # end so the print function does not print a new line each time
            print(grid[x][y],end="")


printGrid(grid)