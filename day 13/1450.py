from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i, j in zip(startTime, endTime):
            if i <= queryTime and j >= queryTime:
                res += 1

        return res

print( Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4) )