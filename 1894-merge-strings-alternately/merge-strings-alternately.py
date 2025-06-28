class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        res =[]
        length = m+n

        for i in range(0, length):
            if i < m:
                res+=word1[i]
            if i<n:
                res+=word2[i]
        return "".join(res)
            