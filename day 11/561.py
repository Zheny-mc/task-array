from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summa = 0
        for i in range(0, len(nums), 2):
            summa += nums[i]
        return summa

print( Solution().arrayPairSum(nums = [1,4,3,2]) )
