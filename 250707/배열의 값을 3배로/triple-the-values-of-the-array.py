matrix = []
rows = 3
cols = 3

for i in range(rows):
    row_data = list(map(int,input().split()))
    matrix.append(row_data)

new_matrix = [
    [element*3 for element in row]
    for row in matrix
]

for i in range(rows):
    for j in range(cols):
        print(new_matrix[i][j],end=" ")
    print()