def resolve():
    n = int(input())
    D = [int(input()) for _ in range(n)]

    print(len(set(D)))

if __name__ == "__main__":
    resolve()