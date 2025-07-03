n = int(input())
check = 1
for i in range(1,n+1):
    for j in range(0,i):
        print(check, end=" ")
        check += 1
    print()