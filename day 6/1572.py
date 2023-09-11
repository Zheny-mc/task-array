from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summa = 0

        for i in range(len(mat)):
            summa += mat[i][i]
            j = len(mat) - i - 1
            if i != j:
                summa += mat[i][j]

        return summa


print(Solution().diagonalSum([[1,2,3], [4,5,6], [7,8,9]]))