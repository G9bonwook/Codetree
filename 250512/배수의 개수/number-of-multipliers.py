numbers = []

for i in range(10):
    numbers.append(int(input()))

count_3 = 0
count_5 = 0

for i in range(10):
    if(numbers[i] % 15 == 0):
        count_3 += 1
        count_5 += 1
    elif(numbers[i] % 3 == 0):
        count_3 += 1
    elif(numbers[i] % 5 == 0):
        count_5 += 1
    else:
        continue

print(f"{count_3} {count_5}")
