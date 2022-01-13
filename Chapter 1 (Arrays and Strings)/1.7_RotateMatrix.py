import math


def rotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    length = math.floor(len(matrix[0]) / 2)
    for i in range(len(matrix)):
        for j in range(length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix) - 1 - j]
            matrix[i][len(matrix) - 1 - j] = temp
    return matrix


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotateMatrix(test))
