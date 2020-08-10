def resolve():
    N, K = map(int, input().split())
    candy_counter = [0] * N

    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for i in A:
            candy_counter[i-1] += 1

    ans = 0
    for i in candy_counter:
        if i == 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()