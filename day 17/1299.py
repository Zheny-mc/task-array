from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr)-1, -1, -1):
            temp = mx
            mx = max(mx, arr[i])
            arr[i] = temp
        return arr

print( Solution().replaceElements( arr = [17,18,5,4,6,1] ) )


