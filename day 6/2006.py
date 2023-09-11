from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    res += 1
        return res

print( Solution().countKDifference(nums = [1,2,2,1], k = 1) )

print([1, 2, 3, 4, 5, 6][:3])