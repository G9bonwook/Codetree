rows = 3
cols = 3

matrixA = []
matrixB = []

for i in range(rows):
    row_data = list(map(int,input().split()))
    matrixA.append(row_data)

input()

for i in range(rows):
    row_data = list(map(int,input().split()))
    matrixB.append(row_data)

matrixC = []

for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(matrixA[i][j] * matrixB[i][j])
    matrixC.append(new_row)

for row in matrixC:
    print(*row)

