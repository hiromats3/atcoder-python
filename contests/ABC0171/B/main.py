def resolve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    p.sort()
    print(sum(p[:K]))

if __name__ == "__main__":
    resolve()