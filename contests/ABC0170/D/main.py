def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    a = [0] * 1000005
    A_max = A[-1]

    for i in A:
        for j in range(1, A_max//i + 1):
            a[i * j] += 1

    ans = 0
    for i in A:
        if a[i] == 1:
            ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()