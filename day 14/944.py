from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    res += 1
                    break
        return res


print( Solution().minDeletionSize(strs = ["cba","daf","ghi"]) )
