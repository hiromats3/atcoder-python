def resolve():
    n, a, b = map(int, input().split())

    count = 0
    for i in range(1, n+1):
        s = sum(map(int, list(str(i))))
        if (a <= s <= b):
            count += i
    print(count)

if __name__ == "__main__":
    resolve()