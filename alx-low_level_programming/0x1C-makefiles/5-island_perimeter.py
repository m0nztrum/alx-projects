#!/usr/bin/python3
"""
module containing the function island perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of an island
    The grid represents water by 0 and 1 for land
    Args:
        grid(list): a list of integers representing the island
    Returns:
        The perimeter of the island defined in grid
    """
    height = len(grid)
    width = len(grid[0])

    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    return size * 4 - edges * 2
