def numIdenticalPairs(nums) -> int:
    res = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                res.append((i, j))
    return len(res)


if __name__ == '__main__':
    print( numIdenticalPairs([1,1,1,1]) )