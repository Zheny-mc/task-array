from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.i = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        str = []
        self.stream[idKey] = value
        while ( self.i < len(self.stream) and self.stream[self.i] != ""):
            str.append(self.stream[self.i])
            self.i += 1
        return str

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dct = { indices[i]: s[i]  for i in range(len(s)) }

        res = []
        os: OrderedStream = OrderedStream(len(s))
        for key, val in dct.items():
            res += os.insert(key, val)

        return ''.join(res)

print( Solution().restoreString(s="codeleet", indices=[4,5,6,7,0,2,1,3]) )