from numba import jit

@jit
def resolve():
    N = int(input())

    ans = 0
    for n in range(1, N+1):
        for m in range(n, N+1, n):
            ans += m
    print(ans)

if __name__ == "__main__":
    resolve()