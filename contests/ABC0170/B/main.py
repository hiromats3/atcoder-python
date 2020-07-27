def resolve():
    x, y = map(int, input().split())

    ans = 'No'
    for kame in range(x + 1):
        tsuru = x - kame
        if kame * 4 + tsuru * 2 == y:
            ans = 'Yes'
            break
    print(ans)

if __name__ == "__main__":
    resolve()