def resolve():
    N = int(input())
    c = input()

    ans = 0
    lp = 0
    rp = N-1
    try:
        while lp < rp:
            while lp < N and c[lp] == "R":
                lp += 1
            while rp > -1 and c[rp] == "W":
                rp -= 1
            if lp < rp:
                ans += 1
                lp += 1
                rp -= 1
    except Exception as err:
        print(err)
        print(c, lp, rp)
    print(ans)

if __name__ == "__main__":
    resolve()