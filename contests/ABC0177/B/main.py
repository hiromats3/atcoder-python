def resolve():
    S = input()
    T = input()

    ans = 1000
    for i in range(len(S) - len(T) + 1):
        x = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                x += 1
        ans = min(ans, x)
    print(ans)

if __name__ == "__main__":
    resolve()