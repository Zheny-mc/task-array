from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([nums[i]**2 for i in range(len(nums)) if len(nums) % (i+1) == 0])


print( Solution().sumOfSquares(nums = [1,2,3,4]) )