from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        technicals = []
        for i in items:
            technicals.append( { "type": i[0], "color": i[1], "name": i[2] } )

        k = 0
        for tech in technicals:
            if tech[ruleKey] == ruleValue:
                k += 1

        return k

print( Solution().countMatches(
    items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
    ruleKey = "color",
    ruleValue = "silver") )