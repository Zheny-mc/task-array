from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dct = {h: n for n, h in zip(names, heights)}
        heights.sort(reverse=True)
        return [dct[i] for i in heights]


print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))