from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return -1

        mx = max(nums)
        mn = min(nums)

        for i in nums:
            if i != mx and i != mn:
                return i

        return -1


print( Solution().findNonMinOrMax(nums = [3,2,1,4]) )

