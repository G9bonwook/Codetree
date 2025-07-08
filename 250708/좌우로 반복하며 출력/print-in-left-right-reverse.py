n = int(input())

matrix = []
cnt = 1

for i in range(n): 
    row = []
    for j in range(n):
        row.append(cnt)
        cnt += 1
    if i % 2 == 1:
        row.reverse() 
    matrix.append(row)
    cnt = 1   


for row in matrix:
    for element in row:
        print(element,end="")
    print()