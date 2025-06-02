string = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()
cnt = 0

for i in range(5):
    if string[i][2] == a or string[i][3] == a:
        print(string[i])
        cnt += 1

print(cnt)