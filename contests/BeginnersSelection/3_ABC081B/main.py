def resolve():
    _ = int(input())
    A = set(map(int, input().split()))

    def include_odd(l:set):
        for i in l:
            if (i % 2 == 1):
                return True
        return False

    count = 0
    while include_odd(A) == False:
        A = set(i / 2 for i in A)
        count += 1
    print(count)

if __name__ == "__main__":
    resolve()