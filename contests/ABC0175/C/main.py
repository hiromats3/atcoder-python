import math

def resolve():
    X, K, D = map(int, input().split())
    X = abs(X)

    s = int(X / D)
    if X - D*s >= X - D*(s+1):
        v0 = abs(X - D*s)
        v1 = abs(X - D*(s+1))
    else:
        s = s+1
        v1 = abs(X - D*s)
        v0 = abs(X - D*(s+1))

    ans = 0
    if K < s:
        ans = X - (K * D)
    else:
        if (K - s) % 2 == 0:
            ans = v0
        else:
            ans = v1
    print(ans)

if __name__ == "__main__":
    resolve()