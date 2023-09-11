import collections
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dct_allowed = collections.Counter(allowed)

        res = 0
        for w in words:
            flag = True
            for letter in w:
                if letter not in dct_allowed:
                    flag = False
                else:
                    continue
            if flag:
                res += 1

        return res

print( Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]) )