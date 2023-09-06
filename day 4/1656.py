from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.i = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        str = []
        self.stream[idKey-1] = value
        while ( self.i < len(self.stream) and self.stream[self.i] != ""):
            str.append(self.stream[self.i])
            self.i += 1
        return str

res = []

os: OrderedStream = OrderedStream(5)
res += os.insert(3, "ccccc") # Inserts (3, "ccccc"), returns [].
res += os.insert(1, "aaaaa") # Inserts (1, "aaaaa"), returns ["aaaaa"].
res += os.insert(2, "bbbbb") # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
res += os.insert(5, "eeeee") # Inserts (5, "eeeee"), returns [].
res += os.insert(4, "ddddd") # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].

print(res)