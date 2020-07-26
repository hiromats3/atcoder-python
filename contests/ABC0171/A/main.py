import re

def resolve():
    alpha = input()

    ans = "A" if re.match(r'[A-Z]', alpha) is not None else "a"
    print(ans)

if __name__ == "__main__":
    resolve()