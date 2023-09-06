from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    maxim = 0
    for lst_score in accounts:
        summa = sum(lst_score)
        maxim = max(maxim, summa)
    return maxim


if __name__ == '__main__':
    print( maximumWealth([[1,2,3],[3,2,1]]) )