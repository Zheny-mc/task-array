from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dct = Counter(nums)
        for i in dct.values():
            if i % 2 == 1:
                return False
        return True


print( Solution().divideArray(nums = [3,2,3,2,2,2]) )