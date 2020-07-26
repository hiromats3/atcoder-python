def resolve():
    N = int(input())
    print((1000 - N % 1000) % 1000)

if __name__ == "__main__":
    resolve()