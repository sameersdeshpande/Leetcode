class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        while l < r:
            if s[l]!=s[r]:
                a = s[l+1:r+1]
                b = s[l:r]
                return a==a[::-1] or b== b[::-1]
            l=l+1
            r=r-1
        return True