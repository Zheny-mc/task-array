from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        res_k = 0

        check_word = lambda l: l == 'a' or l == 'e'or l == 'i' or l == 'o' or l == 'u'

        for i in range(left, right + 1):
            if check_word(words[i][0]) and check_word(words[i][-1]):
                res_k += 1

        return res_k

print( Solution().vowelStrings(words = ["are","amy","u"], left = 0, right = 2) )