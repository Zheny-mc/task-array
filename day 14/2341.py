from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_num = Counter(nums)

        res = [0, 0]
        for val, c  in count_num.items():
            res[0] += c // 2
            res[1] += c % 2
        return res




print( Solution().numberOfPairs(nums = [1,3,2,1,3,2,2]) )