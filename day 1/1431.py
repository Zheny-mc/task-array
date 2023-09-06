from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_c = max(candies)
    return [c + extraCandies >= max_c for c in candies]

if __name__ == '__main__':
    print( kidsWithCandies([2,3,5,1,3], 3) )