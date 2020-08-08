import math

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = []

    if K == 0:
        print(A[-1])
        return
    else:
        temp = A.pop(-1) / 2
        B.append(temp)
        B.append(temp)

    for _ in range(K - 1):
        try:
            a = A[-1]
            b = B[0]
        except Exception as err:
            print(err)
            print(A, B)
            return

        temp = A.pop(-1) if a > b else B.pop(0)
        temp /= 2
        for i in range(len(B)):
            if temp > B[i]:
                B.insert(i, temp)
                B.insert(i, temp)
                temp = 0
                break
        if temp != 0:
            B.insert(i, temp)
            B.insert(i, temp)
    
    ans = B[0]
    if len(A) > 0 and A[-1] > ans:
        ans = A[-1]

    print(math.ceil(ans))

if __name__ == "__main__":
    resolve()