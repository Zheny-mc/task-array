from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 0
            dct[i] += 1

        for k, val in dct.items():
            if val == len(nums) // 2:
                return k
        return -1

print(Solution().repeatedNTimes(nums = [1,2,3,3]))
