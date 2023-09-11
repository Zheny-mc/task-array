from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str):
        if len(words) != len(s):
            return False
        for i, f_chr in enumerate(words):
            if f_chr[0] != s[i]:
                return False

        return True




print(Solution().isAcronym(words = ["alice","bob","charlie"], s = "abc"))