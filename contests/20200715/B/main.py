def resolve():
    a, b, c = map(int, input().split())
    k = int(input())
    
    for _ in range(k):
        if (a >= b):
            b *= 2
        elif (b >= c):
            c *= 2
    
    if(a < b < c):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    resolve()