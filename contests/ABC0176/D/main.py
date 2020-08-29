from collections import deque

def resolve():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = []
    for _ in range(H):
        S.append([s for s in input()])

    # 座標と配列番号を揃える
    Ch -= 1
    Cw -= 1
    Dh -= 1
    Dw -= 1
    # 上下左右の移動で楽する工夫
    walk = [(-1,0), (0,-1), (1,0), (0,1)]
    warp = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),
        (-1,-2), (-1,-1), (-1,1), (-1,2),
        (0,-2), (0,2),
        (1,-2), (1,-1), (1,1), (1,2),
        (2,-2), (2,-1), (2,0), (2,1), (2,2)]

    # コスト格納用の盤面
    INF = 10**9
    dist = [[INF] * W for _ in range(H)]
    dist[Ch][Cw] = -1

    # dequeの定義、(h座標, w座標, コスト)のタプルを格納する
    deq = deque()
    deq.append((Ch, Cw, 0))

    while len(deq) > 0:
        (h, w, d) = deq.popleft()
        # 探索済みマスかどうか
        if dist[h][w] < d and dist[h][w] != -1:
            continue
        # コスト0の移動を検証
        for (dh, dw) in walk:
            nh = h + dh
            nw = w + dw
            # 盤面外かどうか
            if (nh < 0) or (nw < 0) or (nh >= H) or (nw >= W):
                continue
            # 道があるかどうか
            if S[nh][nw] == '#':
                continue
            # 探索済みかどうか
            if dist[nh][nw] <= d:
                continue
            dist[nh][nw] = d
            deq.appendleft((nh, nw, d))
        # コスト1の移動を検証
        for (dh, dw) in warp:
            nh = h + dh
            nw = w + dw
            # 盤面外かどうか
            if (nh < 0) or (nw < 0) or (nh >= H) or (nw >= W):
                continue
            # 道があるかどうか
            if S[nh][nw] == '#':
                continue
            # 探索済みかどうか
            if dist[nh][nw] <= d+1:
                continue
            dist[nh][nw] = d+1
            deq.append((nh, nw, d+1))
    ans = dist[Dh][Dw]
    if ans == INF:
        ans = -1
    print(ans)

if __name__ == "__main__":
    resolve()