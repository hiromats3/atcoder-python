import math

def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    total = 0
    for i in range(1, N):
        total += A[N - 1 - math.floor(i/2)]
    print(total)

if __name__ == "__main__":
    resolve()