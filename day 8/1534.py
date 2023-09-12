from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr) - 1):
                for k in range(j+1, len(arr)):
                    if not (abs(arr[i] - arr[j]) <= a):
                        continue
                    if not (abs(arr[j] - arr[k]) <= b):
                        continue
                    if not (abs(arr[i] - arr[k]) <= c):
                        continue
                    res += 1
        return res

print(Solution().countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))