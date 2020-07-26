def resolve():
    N = int(input())

    ans = 0
    for i in range(1, N+1):
        n = N // i
        ans += i * (n + 1) * n // 2
    print(ans)

if __name__ == "__main__":
    resolve()