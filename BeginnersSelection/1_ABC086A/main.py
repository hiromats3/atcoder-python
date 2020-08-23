def resolve():
    a, b = map(int, input().split())
    r = "Even" if (a * b % 2 == 0) else "Odd"
    print(r)

if __name__ == "__main__":
    resolve()