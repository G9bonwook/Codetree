rows = 4
cols = 4

matrix = [list(map(int,input().split())) for _ in range(rows)]

cnt = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] % 5 == 0:
            cnt += 1

print(cnt)