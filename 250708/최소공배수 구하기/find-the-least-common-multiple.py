n, m = map(int, input().split())
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    print(int(a * b / gcd(a, b))) 


lcm(n,m)
