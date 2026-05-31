# Your task is to construct an n \times n grid where each square has the smallest nonnegative integer that does not appear to the left on the same row or above on the same column.

import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    

# Problem: Given an n x n grid, construct a grid filled with non-negative integers such that the MEX of each row equals a given target value m. The MEX (Minimum Excluded Value) is the smallest non-negative integer not present in a set.

n = int(input())

grid = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        mex = set(range(n+50))  # Possible values for MEX
        # print(mex,i,j)
        for k in range(i):
            mex.discard(grid[k][j])
        for k in range(j):
            mex.discard(grid[i][k])
        # print(i,j)
        # if (i == 2 and j ==4):
        #     for row in grid:
        #         print(*row)
        grid[i][j] = min(mex)

for row in grid:
    print(*row)
