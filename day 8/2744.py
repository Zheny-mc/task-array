from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        used = set()
        res = 0

        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in used or words[j] in used:
                    continue

                if words[i] == words[j][::-1]:
                    used.add(words[i])
                    used.add(words[j])
                    res += 1
        return res


print(Solution().maximumNumberOfStringPairs(words = ["cd","ac","dc","ca","zz"]))