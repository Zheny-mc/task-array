from heapq import heapify, heappop
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dct = {i: j for i, j in nums1}
        for i, j in nums2:
            if i not in dct:
                dct[i] = 0
            dct[i] += j

        tmp = [(k, v) for k, v in dct.items()]
        heapify(tmp)

        res = []
        while tmp:
            res.append(heappop(tmp))
        return res




print( Solution().mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]) )