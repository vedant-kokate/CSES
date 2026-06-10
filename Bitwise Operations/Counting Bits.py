import sys

def count_bits(n: int) -> int:
    total = 0
    while n > 0:
        p = n.bit_length() - 1
        power = 1 << p
        total += p * (power >> 1) + (n - power + 1)
        n -= power
    return total

num = int(sys.stdin.readline())
print(count_bits(num))
