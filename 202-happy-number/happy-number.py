class Solution:
    def isHappy(self, n: int) -> bool:
        
        def squares(n:int)->int:
            total = 0
            while n>0:
                digit= n%10
                total += digit*digit
                n//=10
            return total
        
        seen = set()

        while n!=1:
            n = squares(n)
            if n in seen:
                return False
            seen.add(n)
        return True

       
    


