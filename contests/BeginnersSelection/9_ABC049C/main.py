import re

def resolve():
    s = input()
    r_s = s[::-1]

    p = re.compile(r'(maerd|remaerd|esare|resare)')
    if(len(p.sub('', r_s)) <= 0):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    resolve()