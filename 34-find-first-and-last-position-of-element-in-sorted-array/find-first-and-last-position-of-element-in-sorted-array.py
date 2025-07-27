class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target,findfirst):
            left,right = 0, len(nums)-1
            result = -1

            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    result = mid
                    if findfirst:
                        right = mid -1
                    else:
                        left = mid+1
                elif nums[mid]<target:
                    left = mid +1
                else:
                    right = mid -1
            return result
        
        first = binarySearch(nums,target, True)
        last = binarySearch(nums, target, False)
        return [first, last]
