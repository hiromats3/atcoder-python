def resolve():
    X = int(input())

    account = 100
    t = 0
    while account < X:
        t += 1
        r = str(account)[0:-2]
        account += int(r)
    print(t)

if __name__ == "__main__":
    resolve()