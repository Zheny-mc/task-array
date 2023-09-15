from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd_rem_division(min(nums), max((nums)))

    def gcd_rem_division(self, num1, num2):
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return num1 or num2


print( Solution().findGCD(nums = [2,5,6,9,10]) )
