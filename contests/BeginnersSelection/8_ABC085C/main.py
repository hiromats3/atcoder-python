def resolve():
    N, Y = map(int, input().split())

    if (Y > N * 10000):
        print('-1 -1 -1')
        return
    for x in range(N+1):
        for y in range(N+1-x):
            z = N - x - y
            total = x * 10000 + y * 5000 + z * 1000
            if (total == Y):
                print(f'{x} {y} {z}')
                return
    print('-1 -1 -1')

if __name__ == "__main__":
    resolve()