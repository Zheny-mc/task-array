from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for w in words:
            if s.find(w) == 0:
                res += 1

        return res

print( Solution().countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc") )