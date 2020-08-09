def resolve():
    S = input()
    T = input()

    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    resolve()