from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = lambda p1, p2: max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

        res = 0
        for i_p in range(len(points)-1):
            res += distance(points[i_p], points[i_p+1])

        return res

print( Solution().minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]) )
