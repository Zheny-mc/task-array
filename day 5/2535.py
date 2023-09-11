from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_nums = sum(nums)

        lst_num = []
        for num in nums:
            lst_num += map(int, str(num))

        sum_lst_num = sum(lst_num)

        return abs(sum_nums - sum_lst_num)


print(Solution().differenceOfSum(nums = [1,15,6,3]))

