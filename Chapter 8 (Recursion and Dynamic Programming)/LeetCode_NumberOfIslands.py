def callDFS(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
        return 0

    grid[i][j] = '0'

    return 1 + callDFS(grid, i + 1, j) + callDFS(grid, i - 1, j) + callDFS(grid, i, j + 1) + callDFS(grid, i, j - 1)


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if grid is None:
        return 0
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count = max(callDFS(grid, i, j), count)
    return count


maze = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(maze))
