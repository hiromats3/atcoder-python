def resolve():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]

    counter = 0
    for mask_row in range(int(1 << H) - 1):
        for mask_col in range(int(1 << W) - 1):
            black = 0
            for x in range(H):
                if f'{mask_row:b}'.zfill(H)[x] == '1':
                    continue
                for y in range(W):
                    if f'{mask_col:b}'.zfill(W)[y] == '1':
                        continue
                    if c[x][y] == '#':
                        black += 1
            if black == K:
                counter += 1
    print(counter)

if __name__ == "__main__":
    resolve()