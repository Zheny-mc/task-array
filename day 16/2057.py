from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            if i % 10 == val:
                return i
        return -1

print( Solution().smallestEqual(nums = [0,1,2]) )