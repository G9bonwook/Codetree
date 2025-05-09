a, b = map(int, input().split())
arr = []
arr.append(a)
arr.append(b)

for i in range(2, 10):
    arr.append(arr[i-2] + arr[i-1])
    if(arr[i] >= 10):
        arr[i] = arr[i] - 10

for i in range(len(arr)):
    print(arr[i],end=" ")
