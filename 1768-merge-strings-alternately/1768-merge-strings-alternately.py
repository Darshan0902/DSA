class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1),len(word2))
        m = len(word1)
        n = len(word2)
        res = ""
        for i in range(0,max_length):
            if i < m:
                res+=word1[i]
            if i < n:
                res+=word2[i]
        return res
