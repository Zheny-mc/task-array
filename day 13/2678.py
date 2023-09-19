from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            if int(d[-4:-3+1]) > 60:
                res += 1
        return res

print(Solution().countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"]))
