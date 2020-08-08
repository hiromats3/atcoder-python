import math

def resolve():
    N, D = map(int, input().split())

    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        dist = math.sqrt(x*x + y*y)
        if dist <= D:
            ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()