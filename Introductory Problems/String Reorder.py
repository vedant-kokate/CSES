import sys

def main():
    data = sys.stdin.read().split()
    s = data[0].strip()
    n = len(s)
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 65] += 1

    limit = (n + 1) // 2
    if max(counts) > limit:
        return("-1")

    result = [''] * n
    prev = -1
    for i in range(n):
        # print(result)
        max_count = 0
        second_max = 0
        max_index = -1
        val = -1
        for j in range(26):
            if counts[j] > max_count:
                second_max = max_count
                max_count = counts[j]
                max_index = j
            elif counts[j] > second_max:
                second_max = counts[j]

        for j in range(26):
            if counts[j]==0 or prev == j:
                continue
            if j != max_index and max_count > ((n-i)//2):
                # print("here")
                continue
            if j == max_index and second_max > ((n-i)//2):
                continue
            val = j + 65
            prev = j
            break

        if val == -1:
            return("-1")
        result[i] = chr(val)
        counts[val - 65] -= 1
    return "".join(result)

    sys.stdout.write("".join(result))


if __name__ == "__main__":
    sys.stdout.write(main())
