

class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        res = 0
        s = set(nums)
        for i in range(len(nums)):
            if (nums[i] - diff) in s and (nums[i] - 2 * diff) in s:
                res += 1
        return res

print(Solution().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))

