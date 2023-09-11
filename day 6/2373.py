from itertools import product
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid) - 2
        res = [[0]*N for _ in range(N)]

        for i, j in product(range(N), range(N)):
            res[i][j] = max(grid[r][c] for r, c in product(range(i, i+3), range(j, j+3)))

        return res

print( Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]) )