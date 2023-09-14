from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l=[]
        for i in rectangles:
            l.append(min(i[0],i[1]))
        return l.count(max(l))

print(Solution().countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]]))