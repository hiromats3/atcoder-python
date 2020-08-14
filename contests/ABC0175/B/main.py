def resolve():
    N = int(input())
    L = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        for j in range(i, N):
            if L[i] == L[j]:
                continue
            for k in range(j, N):
                if L[k] == L[i] or L[k] == L[j]:
                    continue
                s = sorted([L[i], L[j], L[k]])
                if s[0] + s[1] > s[2]:
                    ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()