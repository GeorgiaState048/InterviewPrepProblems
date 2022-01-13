import random
rows = 3
cols = 3
matrix = []
for i in range(rows):
    arr = []
    for j in range(cols):
        arr.append(random.randrange(10))
    matrix.append(arr)

for i in matrix:
    print(i)

rectangular = []
for i in range(rows):
    for j in range(cols):
        rectangular.append(matrix[i][j])
print(rectangular)
mTest = matrix[2][2]
mTest1 = matrix[1][1]

print(mTest)

