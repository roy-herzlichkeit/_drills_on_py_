import sys

input = sys.stdin.readline


def solve():
    line = input().split()
    if len(line) >= 2:
        n, q = map(int, line[:2])
    else:
        n = int(line[0])
        q = int(input())

    arr = []
    while len(arr) < n:
        parts = input().split()
        if not parts:
            continue
        arr.extend(map(int, parts))

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    out = []
    for _ in range(q):
        parts = input().split()
        while not parts:
            parts = input().split()
        a, b = map(int, parts[:2])
        out.append(str(prefix_sum[b] - prefix_sum[a - 1]))

    sys.stdout.write("\n".join(out))


def main():
    solve()


if __name__ == "__main__":
    main()