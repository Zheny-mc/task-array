from typing import List

def decompressRLElist(nums: List[int]) -> List[int]:
    arr = []
    for i in range(1, len(nums), 2):
        arr += [nums[i]] * nums[i-1]
    return arr

print(decompressRLElist(nums = [1,2,3,4]))