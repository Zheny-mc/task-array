from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [0]*len(prices)
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    res[i] = prices[i] - prices[j]
                    break
                else:
                    res[i] = prices[i]
        res[-1] = prices[-1]
        return res


print( Solution().finalPrices(prices = [8,4,6,2,3]) )