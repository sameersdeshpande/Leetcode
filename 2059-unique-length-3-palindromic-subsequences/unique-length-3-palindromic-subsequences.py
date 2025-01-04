class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for l in letters:
            i,j = s.index(l),s.rindex(l)
            between = set()

            for k in range(i+1,j):
                between.add(s[k])
            ans+= len(between)
        return ans