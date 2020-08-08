def resolve():
    N = int(input())
    c = input()

    r = w = 0
    for i in range(N):
        if c[i] == "R":
            r += 1

    ans = max(r, w)
    for i in range(N):
        if c[i] == "R":
            r -= 1
        else:
            w += 1
        current = max(r, w)
        ans = min(ans, current)
    print(ans)

if __name__ == "__main__":
    resolve()