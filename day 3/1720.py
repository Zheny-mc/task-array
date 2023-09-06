from typing import List


def decode(encoded: List[int], first: int) -> List[int]:
    encoded.insert(0, first)
    for i in range(len(encoded)-1):
        encoded[i+1] ^= encoded[i]
    return encoded


print( decode(encoded = [1,2,3], first = 1) )