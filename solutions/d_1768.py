from itertools import chain

class Solution:
    def mergeAlternately(self, word1:str, word2:str) -> str:
        word_2n = ''.join(chain.from_iterable(zip(word1, word2)))
        n = len(word_2n) // 2
        word_pp = word1[n:] + word2[n:]
        return word_2n + word_pp