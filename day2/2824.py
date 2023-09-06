from typing import List

def countPairs(nums: List[int], target: int) -> int:
    k = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < target:
                k += 1
    return k



if __name__ == '__main__':
    print( countPairs(nums = [-1,1,2,3,1], target = 2) )