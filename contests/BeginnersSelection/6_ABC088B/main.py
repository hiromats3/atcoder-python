def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += A[i]
        else:
            bob += A[i]
    print(alice - bob)

if __name__ == "__main__":
    resolve()