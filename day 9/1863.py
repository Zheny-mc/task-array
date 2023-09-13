from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)

    def helper(self, nums, level, currentXOR):
        if level == len(nums):
            return currentXOR

        inc = self.helper(nums, level+1, currentXOR^nums[level])
        ecx = self.helper(nums, level+1, currentXOR)

        return inc + ecx

print( Solution().subsetXORSum(nums = [1,3]) )