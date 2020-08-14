def resolve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -100100100
    for i in range(N):
        node_set = set()
        n = P[i]
        score = 0
        t = []
        while n not in node_set:
            score += C[n-1]
            t.append(score)
            node_set.add(n)
            n = P[n-1]

        if K < len(t):
            max_t = max(t[:K])
        else:
            max_t = max(t)
            if t[-1] > 0:
                temp = t[-1] * int(K / len(t)) + max([0] + t[:K%len(t)])
                max_t = max(max_t, temp)
        ans = max(ans, max_t)

    print(ans)


if __name__ == "__main__":
    resolve()