from typing import List


def finalValueAfterOperations(operations: List[str]):
    dct = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}
    res = 0
    for oper in operations:
        res += dct[oper]
    return res


if __name__ == '__main__':
    print( finalValueAfterOperations(["--X","X++","X++"]) )


