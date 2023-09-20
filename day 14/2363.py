from typing import List, Tuple


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dct = {}
        def helper(items):
            for val, c in items:
                if val not in dct:
                    dct[val] = 0
                dct[val] += c

        helper(items1)
        helper(items2)

        return [ [i, dct[i]] for i in sorted(dct) ]





print( Solution().mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]) )