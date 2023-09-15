from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        set_diff = set_nums1 & set_nums2

        get_res = lambda arr: list(arr - set_diff)
        return [get_res(set_nums1), get_res(set_nums2)]

print(Solution().findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
