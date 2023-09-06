from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        k = 0
        for i in nums:
            if i < num:
                k += 1
        res.append(k)
    return res

print( smallerNumbersThanCurrent(nums = [8,1,2,2,3]) )