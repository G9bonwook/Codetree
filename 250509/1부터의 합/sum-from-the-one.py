N = int(input())
sum = 0
for i in range (1,101):
    sum += i
    if sum < N:
        continue
    else:
        print(i)
        break