import math

def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def _f(length: int) -> bool:
        count = 0
        for a in A:
            count += int((a-1) / length)
        return count <= K

    l = 0
    r = 10**9
    while (r-l) > 1:
        mid = (l+r) // 2
        if _f(mid):
            r = mid
        else:
            l = mid
    print(r)

if __name__ == "__main__":
    resolve()