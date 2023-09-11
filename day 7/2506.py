from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)-1):
            set_word = set(words[i])
            for j in range(i+1, len(words)):
                if set_word == set(words[j]):
                    res += 1
        return res


print( Solution().similarPairs(words = ["aba","aabb","abcd","bac","aabc"]) )