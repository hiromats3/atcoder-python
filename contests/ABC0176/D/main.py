def resolve():
    H, W, M = map(int, input().split())
    pos = []
    for _ in range(M):
        pos.append(list(map(int, input().split())))

    h_totals = [0] * (H+1)
    w_totals = [0] * (W+1)
    overlap = [set() for _ in range(H+1)]

    for ph, pw in pos:
        h_totals[ph] += 1
        w_totals[pw] += 1
        overlap[ph].add(pw)

    max_h = -1
    max_w = -1
    h_list = []
    w_list = []
    for i in range(1, H+1):
        if h_totals[i] > max_h:
            max_h = h_totals[i]
            h_list = [i]
        elif h_totals[i] == max_h:
            h_list.append(i)
    for j in range(1, W+1):
        if w_totals[j] > max_w:
            max_w = w_totals[j]
            w_list = [j]
        elif w_totals[j] == max_w:
            w_list.append(j)

    for i in h_list:
        for j in w_list:
            if j not in overlap[i]:
                print(max_h + max_w)
                return
    print(max_h + max_w - 1)

if __name__ == "__main__":
    resolve()