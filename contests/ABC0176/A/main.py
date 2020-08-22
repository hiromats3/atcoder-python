import math

def resolve():
    N, X, T = map(int, input().split())

    ans = math.ceil(N / X) * T
    print(ans)

if __name__ == "__main__":
    resolve()