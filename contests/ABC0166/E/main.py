def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)

    ans = 0
    for i in range(1, N+1):
        for j in range(A[i]+i+1, N+1):
            if j - i == A[j] + A[i]:
                ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()