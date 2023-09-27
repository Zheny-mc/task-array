from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = -10**9
        for s in strs:
            if s.isdigit():
                mx = max(int(s), mx)
            else:
                mx = max(len(s), mx)
        return mx


print( Solution().maximumValue(strs = ["alic3","bob","3","4","00000"]) )