def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    max_height = A[0]
    for i in range(1, N):
        if max_height < A[i]:
            max_height = A[i]
        else:
            ans += max_height - A[i]
    print(ans)

if __name__ == "__main__":
    resolve()