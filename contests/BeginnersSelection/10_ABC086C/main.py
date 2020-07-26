import math

def resolve():
    N = int(input())
    t = [0] * (N + 1)
    x = [0] * (N + 1)
    y = [0] * (N + 1)
    for i in range(N):
        t[i + 1], x[i + 1], y[i + 1] = map(int, input().split())

    can = True
    for i in range(0, N):
        dt = t[i + 1] - t[i]
        dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
        if (dt < dist):
            can = False
            break
        if (dt % 2 != dist % 2):
            can = False
            break
    print("Yes" if can else "No")

if __name__ == "__main__":
    resolve()
