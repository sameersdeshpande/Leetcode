class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        reverse = 0

        while x>0:
          reverse = reverse*10 + x%10
          x//=10
        
        

        return True if reverse == y else False