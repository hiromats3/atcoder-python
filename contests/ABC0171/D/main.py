def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    a = [0] * 100001
    for i in A:
        a[i] += i

    ans = sum(a)
    for b, c in BC:
        if a[b] == 0:
            print(ans)
            continue
        move = a[b] // b
        a[b] = 0
        a[c] += c * move
        ans += (c - b) * move
        print(ans)

if __name__ == "__main__":
    resolve()