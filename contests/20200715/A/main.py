def resolve():
    rate = int(input())
    if rate < 600:
        print('8')
    elif rate < 800:
        print('7')
    elif rate < 1000:
        print('6')
    elif rate < 1200:
        print('5')
    elif rate < 1400:
        print('4')
    elif rate < 1600:
        print('3')
    elif rate < 1800:
        print('2')
    else:
        print('1')

if __name__ == "__main__":
    resolve()