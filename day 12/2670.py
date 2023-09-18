from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = {nums[0]: 1}

        suffix = {}
        for i in range(1, len(nums)):
            if nums[i] not in suffix:
                suffix[nums[i]] = 0
            suffix[nums[i]] += 1

        res = []
        for i in range(len(nums)):
            res.append( len(prefix) - len(suffix) )

            if i+1 < len(nums):
                next = nums[i+1]
                if next not in prefix:
                    prefix[next] = 0
                prefix[next] += 1

                if next in suffix and suffix[next] == 1:
                    del suffix[next]
                else:
                    suffix[next] -= 1

        return res


print( Solution().distinctDifferenceArray(nums = [1,2,3,4,5]) )