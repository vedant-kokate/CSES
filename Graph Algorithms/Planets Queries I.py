import sys

input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    t = list(map(lambda x: int(x) - 1, input().split()))
    LOG = 31
    up = [t]
    for i in range(1, LOG):
        prev = up[i - 1]
        curr = [0] * n
        for u in range(n):
            curr[u] = prev[prev[u]]
        up.append(curr)
    out = []
    for _ in range(q):
        x, k = map(int, input().split())
        u = x - 1
        bit = 0
        while k:
            if k & 1:
                u = up[bit][u]
            k >>= 1
            bit += 1
        print(u + 1)


if __name__ == '__main__':
    main()
