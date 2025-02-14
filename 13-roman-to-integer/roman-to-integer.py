class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        n = len(s)


        for i in range(n):
            current_value=roman[s[i]]
        
            if i<n-1 and current_value <roman[s[i+1]]:
                value-=current_value
            else:
                value+=current_value
        return value