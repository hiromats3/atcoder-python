class UnionFind():
    def __init__(self, n: int):
        """
        n: ノード数
        """
        self.n = n
        """
        d: UnionFind木のデータ構造
            各要素の根要素を格納するリスト
            根要素の場合は, グループの要素数*-1を格納する
        """
        self.d = [-1] * n

    def find(self, x: int) -> int:
        """
        要素xが属するグループの根を返す
        """
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]

    def unite(self, x: int, y: int) -> bool:
        """
        要素xが属するグループと, 要素yが属するグループを併合する
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        """
        要素x, yが同じグループに属するかどうかを返す
        """
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        """
        要素xが属するグループのサイズ(要素数)を返す
        """
        return -self.d[self.find(x)]

    def members(self, x: int) -> list:
        """
        要素xが属するグループの要素をリストで返す
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def groups(self) -> list:
        """
        すべての根の要素をリストで返す
        """
        return [i for i, x in enumerate(self.d) if x < 0]

    def group_count(self) -> int:
        """
        グループの数を返す
        """
        return len(self.groups())


def resolve():
    N, M = map(int, input().split())

    uf = UnionFind(N)

    for _ in range(M):
        A, B = map(int, input().split())
        uf.unite(A-1, B-1)

    ans = 0
    for i in uf.groups():
        ans = max(ans, uf.size(i))
    print(ans)

if __name__ == "__main__":
    resolve()