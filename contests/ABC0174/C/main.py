def resolve():
    K = int(input())

    m = 7 % K

    ans = -1
    for i in range(1, K+1):
        if m == 0:
            ans = i
            break
        m = (m * 10 + 7) % K
    print(ans)

if __name__ == "__main__":
    resolve()