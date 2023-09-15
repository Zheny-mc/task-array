from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        res = 0
        for j in range(len(grid[0])):
            mx = 0
            for i in range(len(grid)):
                mx = max(mx, grid[i][j])
            res += mx

        return res


print( Solution().deleteGreatestValue(grid = [[1,2,4],[3,3,1]]) )