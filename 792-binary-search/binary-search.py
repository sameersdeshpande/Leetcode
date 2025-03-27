class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,end = 0, len(nums)-1
    
        while end >= left:
            right = (left+end)//2
            if target==nums[right]:
                return right
            elif target > nums[right]:
                left = right+1
            else:
                end = right -1
        return -1