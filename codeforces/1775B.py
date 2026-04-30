import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    mp = {}
    groups = []
    for _ in range(n):
        row = list(map(int, input().split()))
        x = row[0]
        temp = row[1:1 + x]
        groups.append(temp)
        for value in temp:
            mp[value] = mp.get(value, 0) + 1

    ans = "No"
    for group in groups:
        ok = True
        for value in group:
            if mp[value] == 1:
                ok = False
                break
        if ok:
            ans = "Yes"
            break

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()