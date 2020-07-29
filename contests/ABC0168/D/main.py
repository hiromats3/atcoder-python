from collections import deque

def resolve():
    N, M = map(int, input().split())
    to = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    INF = 1001001001
    dist = [INF] * N
    prev = [-1] * N
    dist[0] = 0
    q = deque([0])
    while len(q) > 0:
        i = q.popleft()
        for j in to[i]:
            if dist[j] != INF:
                continue
            dist[j] = dist[i] + 1
            prev[j] = i
            q.append(j)

    print("Yes")
    for i in range(1, N):
        ans = prev[i]
        ans += 1
        print(ans)

if __name__ == "__main__":
    resolve()