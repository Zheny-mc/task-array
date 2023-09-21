from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_Occurency = Counter(arr)
        set_occ = set(count_Occurency.values())
        return len(set_occ) == len(count_Occurency)

print( Solution().uniqueOccurrences(arr = [1,2,2,1,1,3]) )
