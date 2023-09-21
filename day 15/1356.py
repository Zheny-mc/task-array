from heapq import heapify, heappop
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countsOne(n):
            cnt = 0
            while n:
                n = n & n-1
                cnt += 1
            return cnt

        arr = [ (countsOne(i), i) for i in arr]

        heapify(arr)

        res = []
        while arr:
            res.append( heappop(arr)[1] )
        return res

print( Solution().sortByBits(arr = [0,1,2,3,4,5,6,7,8]) )