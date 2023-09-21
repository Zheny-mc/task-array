from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s = set()
        s_nums1 = set(nums1)
        s_nums2 = set(nums2)
        s_nums3 = set(nums3)

        for i in nums1:
            if i in s_nums2 or i in s_nums3:
                s.add(i)

        for i in nums2:
            if i in s_nums1 or i in s_nums3:
                s.add(i)

        for i in nums3:
            if i in s_nums1 or i in s_nums2:
                s.add(i)

        return list(s)


print( Solution().twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]) )