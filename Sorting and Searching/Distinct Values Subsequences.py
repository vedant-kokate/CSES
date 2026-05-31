import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    freq = {}
    for _ in range(n):
        x = int(next(it))
        freq[x] = freq.get(x, 0) + 1
    ans = 1
    for count in freq.values():
        ans = ans * (count + 1) % MOD
    ans = (ans - 1) % MOD
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    main()
