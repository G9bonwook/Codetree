n, m = map(int, input().split())


def GCD(n,m):
    answer = 0
    for i in range(n+1,0,-1):
        if n % i == 0:
            if m % i == 0:
                answer = i
                break
    print(answer)


GCD(n,m)
