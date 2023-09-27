from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [i*i for i in nums]
        res.sort()
        return res


print( Solution().sortedSquares(nums = [-4,-1,0,3,10]) )
