#!/usr/bin/python3
''' ALX INTERVIEW RETURN PERIMITER OF AN ISLAND'''


def island_perimeter(grid):
    ''' perimeter of an island'''
    if not isinstance(grid, list):
        return 0
    perimeter = 0
    rows = len(grid)
    column = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(column):
            if grid[i][j] == 1:
                ''' check sides'''
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == column - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
