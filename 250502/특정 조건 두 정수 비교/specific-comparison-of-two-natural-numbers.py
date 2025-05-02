a,b = map(int, input().split())

result1 = False
result2 = False

if a < b:
    result1 = True

if a == b:
    result2 = True

print(f"{int(result1)} {int(result2)}")