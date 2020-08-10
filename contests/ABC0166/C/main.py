def resolve():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    higher_peeks = [0] * N

    for _ in range(M):
        A, B = map(int, input().split())
        if H[A-1] > H[B-1]:
            higher_peeks[B-1] += 1
        elif H[A-1] < H[B-1]:
            higher_peeks[A-1] += 1
        else:
            higher_peeks[A-1] += 1
            higher_peeks[B-1] += 1

    ans = 0
    for i in higher_peeks:
        if i == 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    resolve()