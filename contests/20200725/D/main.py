def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    account = 1000
    stock = 0

    inc_list = [1 if (A[i] < A[i+1]) else 0 for i in range(n-1)]
    for i in range(n):
        if(i < n-1 and inc_list[i] == 1):
            if(stock == 0):
                stock = int(account / A[i])
                account %= A[i]
        else:
            if(stock != 0):
                account += stock * A[i]
                stock = 0
    print(account)

if __name__ == "__main__":
    resolve()