def ip():
    l = list()
    print("Enter 13 numbers:")
    for _ in range(13):
        ip = int(input())
        l.append(ip)
    t = tuple(l)
    return t

def split(t1):
    l1 = list()
    l2 = list()
    for it in t1:
        l1.append(it) if it % 2 else l2.append(it)
    t2 = (l1, l2)
    return t2

def trim(t):
    (a, *b, c) = t
    return b

def main():
    t = ip()
    print(trim(t))
    print(split(t))

if __name__ == "__main__":
    main()