import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

n,m = get_ints()
mat = []
for _ in range(n):
    string_input = list(input())
    mat.append(string_input)
# print(mat)
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if mat[i][j] == "A":
                mat[i][j] = "B"
            else:
                mat[i][j] = "A"
        else:
            if mat[i][j] == "C":
                mat[i][j] = "D"
            else:
                mat[i][j] = "C"
for row in mat:
    print("".join(row))
