def getPath(maze):
    if not maze or len(maze) == 0:
        return None
    path = []
    failedPoints = set()
    if checkPath(maze, 0, len(maze[0]) - 1, path, failedPoints):  # input destination here. we will work backwards
        return path
    else:
        return None


def checkPath(maze, row, col, path, failedPoints):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 1:
        return False

    point = (row, col)
    if point in failedPoints:
        return False
    else:
        failedPoints.add(point)

    isAtOrigin = (row == len(maze) - 1) and (col == 0)  # in the CTCI example, the origin is the top left corner,
    # but not always the  case

    if (
            isAtOrigin
            or checkPath(maze, row + 1, col, path, failedPoints)
            or checkPath(maze, row - 1, col, path, failedPoints)
            or checkPath(maze, row, col + 1, path, failedPoints)
            or checkPath(maze, row, col - 1, path, failedPoints)):
        path.append(point)
        return True
    return False


matrix = []
for i in range(8):
    arr = []
    for j in range(8):
        arr.append(0)
    matrix.append(arr)

matrix[0][0] = 1
matrix[0][2] = 1
matrix[0][6] = 1
matrix[1][2] = 1
#  matrix[1][5] = 1
matrix[2][1] = 1
matrix[2][2] = 1
matrix[2][4] = 1
matrix[2][5] = 1
matrix[2][7] = 1
matrix[3][1] = 1
matrix[3][2] = 1
matrix[3][5] = 1
matrix[4][1] = 1
matrix[4][2] = 1
matrix[4][3] = 1
matrix[4][5] = 1
matrix[4][7] = 1
matrix[5][2] = 1
matrix[5][3] = 1
matrix[5][5] = 1
matrix[6][0] = 1
matrix[6][6] = 1
matrix[7][2] = 1
matrix[7][3] = 1
matrix[7][4] = 1
matrix[3][7] = 1

for i in matrix:
    print(i)
print(getPath(matrix))
