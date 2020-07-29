def resolve():
    N = int(input())
    mod = N % 10
    if mod == 3:
        print("bon")
    elif mod == 0 or mod == 1 or mod == 6 or mod == 8:
        print("pon")
    else:
        print("hon")

if __name__ == "__main__":
    resolve()