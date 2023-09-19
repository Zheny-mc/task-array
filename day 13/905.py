from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort()
        left_arr = [i for i in nums if i % 2 == 0]
        right_arr = [i for i in nums if i % 2 == 1]
        return left_arr + right_arr

print( Solution().sortArrayByParity(nums = [3,1,2,4]) )
