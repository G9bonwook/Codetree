rows, cols = map(int,input().split())

matrixA = [list(map(int,input().split())) for _ in range(rows)]
matrixB = [list(map(int,input().split())) for _ in range(rows)]

matrixC = []

for i in range(rows):
    new_row = []
    for j in range(cols):
        if (matrixA[i][j] == matrixB[i][j]):
            new_row.append(0)
        else:
            new_row.append(1)
    matrixC.append(new_row)

for row in matrixC:
    print(*row)