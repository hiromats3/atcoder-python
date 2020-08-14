def resolve():
    K = int(input())
    A, B = map(int, input().split())

    for i in range(1, 1001):
        if A <= K*i <= B:
            print("OK")
            return
    print("NG")

if __name__ == "__main__":
    resolve()