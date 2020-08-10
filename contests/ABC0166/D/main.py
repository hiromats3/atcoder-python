def resolve():
    X = int(input())

    for a in range(200):
        for b in range(-199, 199):
            if (a**5 - b**5) == X:
                print(a, b)

if __name__ == "__main__":
    resolve()