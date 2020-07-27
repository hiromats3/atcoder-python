def resolve():
    AB = input().split()
    A = int(AB[0])
    B = int(AB[1].replace('.', ''))
    ans = A * B // 100
    print(ans)

if __name__ == "__main__":
    resolve()