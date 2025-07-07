rows = 4
cols = 4

matrix = [list(map(int,input().split())) for _ in range(rows)]

for i in range(rows):
    sum = 0
    for j in range(cols):
        sum += matrix[i][j]
    print(sum)