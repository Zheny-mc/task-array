from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = -1
        mx = -1
        for i in range(len(mat)):
            sum_s = sum(mat[i])
            if mx < sum_s:
                mx = sum_s
                res = i

        return [res, mx]

print(Solution().rowAndMaximumOnes(mat = [[0,1],[1,0]]))