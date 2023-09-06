from typing import List

def mostWordsFound(sentences: List[str]) -> int:
    max_len = 0
    for sen in sentences:
        max_len = max(max_len, len(sen.split()))

    return max_len


print( mostWordsFound(["alice and bob love leetcode",
                       "i think so too",
                       "this is great thanks very much"]) )