from functools import reduce
from typing import List


def runningSum(nums) -> List[int]:
    res = [nums[0]]
    summa = nums[0]
    for i in range(1, len(nums)):
        summa += nums[i]
        res.append(summa)
    return res


print(runningSum([1,2,3,4]))