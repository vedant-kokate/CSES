import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 

def main():
    x, n = get_ints()
    p = list(get_ints())
    ligths = {}
    sorted_p = sorted(p)
    max_distance = 0
    for i in range(n):
        # left, right
        val = sorted_p[i]
        left = sorted_p[i-1] if i-1 >= 0 else 0
        right = sorted_p[i+1] if i+1 < n else x
        ligths[val] = [left, right ]
        max_distance = max(max_distance, (right - val), (val - left))
    ligths[0] = [0 , sorted_p[0]]
    ligths[x] = [sorted_p[n-1], x]
    max_distance = max(max_distance, sorted_p[0] - 0, x - sorted_p[n-1])
    # print(ligths)
    # print("===========")
    result = []
    for i in reversed(p):
        result.append(max_distance)
        left, right = ligths[i]
        max_distance = max(max_distance, (right -left))
        # print(ligths[i])
        # print(ligths[left], ligths[right])
        ligths[right][0] = left
        ligths[left][1] = right
        # print(ligths)
        # print("===========")

    print(*reversed(result))


if __name__ == "__main__":
    main()
