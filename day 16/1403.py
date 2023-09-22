from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sum_arr = sum(nums)

        tmp_sum = 0
        res = []
        for i in nums:
            if tmp_sum > sum_arr:
                break
            tmp_sum += i
            sum_arr -= i
            res.append(i)

        return res


print(Solution().minSubsequence(nums = [4,3,10,9,8]))