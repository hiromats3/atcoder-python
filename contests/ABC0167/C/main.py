def resolve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        l = list(map(int, input().split()))
        C.append(l[0])
        A.append(l[1:])

    def _judge(pick_pattern: str) -> int:
        price = 0
        level = [0] * M
        # 金額と理解度の合計をそれぞれ求める
        for i in range(N):
            if pick_pattern[i] == "0":
                continue
            price += C[i]
            for j in range(M):
                level[j] += A[i][j]
        # 理解度の目標を達成しているかどうかを判定
        for j in range(M):
            if level[j] < X:
                return -1
        return price

    ans = 1001001001
    for i in range(2**N):
        pick = f"{i:b}".zfill(N)
        price = _judge(pick)
        if price > 0:
            ans = min(price, ans)

    print(ans if (ans < 1001001000) else -1)


if __name__ == "__main__":
    resolve()