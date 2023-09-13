from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
    
print( Solution().countPairs(nums = [3,1,2,2,2,1,3], k = 2) )
