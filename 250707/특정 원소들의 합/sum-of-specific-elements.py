rows = 4
cols = 4

matrix = [list(map(int,input().split())) for _ in range(rows)]
sum = 0

for i in range(0,rows):
    for j in range(0,i+1):
        sum += matrix[i][j]
    
print(sum)
