from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1

            for i in range(m):
                matrix[i][c] += 1


        res = 0
        for row in matrix:
            for val in row:
                if val % 2 == 1:
                    res += 1
        return res

print( Solution().oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]) )