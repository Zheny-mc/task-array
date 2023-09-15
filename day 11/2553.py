from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res += [int(i) for i in str(num)]
        return res


print( Solution().separateDigits(nums = [13,25,83,77]) )