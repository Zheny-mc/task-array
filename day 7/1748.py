from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k if v==1 else 0 for k,v in Counter(nums).items())