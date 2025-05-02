a,b,c = map(int, input().split())

sum = a + b + c
avg = int(sum / 3)
value = sum - avg

print(f"{sum}\n{avg}\n{value}")