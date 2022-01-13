"""Create a square of sides length five in the center of a 9 x 9 matrix"""
import math
import random

matrix = []
for i in range(9):
    arr = []
    for j in range(9):
        arr.append(random.randrange(10))
    matrix.append(arr)


def fillSquare(grid, sideLen):
    length = len(grid)
    center = math.floor(length / 2)
    print(center)
    leftBound = center - math.floor(sideLen / 2)
    topBound = center - math.floor(sideLen / 2)
    rightBound = leftBound + sideLen - 1
    bottomBound = topBound + sideLen - 1

    for row in range(length):
        for col in range(length):
            if bottomBound >= row >= topBound and rightBound >= col >= leftBound:
                matrix[row][col] = 1

    return matrix


# fillSquare(matrix, 7)

for i in matrix:
    print(i)
test = 3
saved = [10]*10
print(saved)
if test == 3:
    saved = [0]*10
print(saved[8])
for i in range(len(matrix)):
    print(matrix[i][2])
