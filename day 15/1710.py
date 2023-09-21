from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_arr = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        result = 0
        for box in sorted_arr:
            if truckSize <= box[0]:
                result += truckSize * box[1]
                break
            result += (box[0] * box[1])
            truckSize -= box[0]

        return result


print(Solution().maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))