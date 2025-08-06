class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        count = 0
        for i in range (len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                count = count +1
        
        if count == len(nums):
            return False
        else:
           return True
        

            
        
        
        