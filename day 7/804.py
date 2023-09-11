from typing import List


class Solution:

    def __init__(self) -> None:
        lst_chr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.alphabet = { chr(i): lst_chr[i % 97] for i in range(97, 97+26) }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()

        for word in words:
            word_to_morze = []
            for i in word:
                word_to_morze.append(self.alphabet[i])

            res.add(''.join(word_to_morze))

        return len(res)




print( Solution().uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]) )
