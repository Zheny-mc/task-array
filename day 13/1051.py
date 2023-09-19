from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)
        res = 0
        for i, j in zip(sorted_h, heights):
            if i != j:
                res += 1
        return res

print( Solution().heightChecker(heights = [1,1,4,2,1,3]) )

