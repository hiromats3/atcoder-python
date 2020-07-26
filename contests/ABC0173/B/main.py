def resolve():
    N = int(input())
    s = [input() for _ in range(N)]
    counter = {
        "AC": 0,
        "WA": 0,
        "TLE": 0,
        "RE": 0,
    }
    for i in range(N):
        counter[s[i]] += 1

    for k, v in counter.items():
        print(f"{k} x {v}")

if __name__ == "__main__":
    resolve()