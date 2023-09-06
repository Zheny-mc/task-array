from typing import List

def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    arr = []
    for i in range(len(nums)):
        if index[i] == len(arr):
            arr.append(nums[i])
        else:
            arr = arr[:index[i]] + [nums[i]] + arr[index[i]:]
    return arr


print( createTargetArray([0,1,2,3,4], index = [0,1,2,2,1]) )